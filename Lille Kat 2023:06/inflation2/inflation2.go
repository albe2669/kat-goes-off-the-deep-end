// Package provides a 100/100 soluton to the inflation2 problem on Kattis
// with a runtime of 0.14 seconds
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var reader = bufio.NewReader(os.Stdin)
var ws = bufio.NewWriter(os.Stdout)

var globalInflation int64 = 0
var table = make(map[int64]int64)
var sum int64 = 0
var totalAmount int64 = 0

func main() {
	totalAmount = readInt64()

	for _, price := range readArrInt64() {
		table[price]++
		sum += price
	}

	days := readInt()
	var inflation int64
	var x, y int64

	for i := 0; i < days; i++ {
		line := readLine()

		if line[0] == 'I' {
			inflation = readInt64From(line[10:])

			globalInflation += inflation
			sum += totalAmount * inflation
		} else {
			tokens := strings.Split(line, " ")
			x = readInt64From(tokens[1])
			y = readInt64From(tokens[2])

			if x != y {
				if _, ok := table[x-globalInflation]; !ok {
					goto printSum
				}

				table[y-globalInflation] += table[x-globalInflation]

				sum += (y - x) * table[x-globalInflation]
				delete(table, x-globalInflation)

			}
		}
	printSum:
		ws.WriteString(fmt.Sprint(sum) + "\n")
	}

	ws.Flush()
}

func readLine() string {
	line, err := reader.ReadString('\n')
	if err != nil {
		panic(err)
	}

	return line[:len(line)-1]
}

func readInt() int {
	nStr, e := reader.ReadString('\n')
	if e != nil {
		panic(e)
	}

	nStr = nStr[:len(nStr)-1]
	n, e := strconv.Atoi(nStr)
	if e != nil {
		panic(e)
	}

	return n
}

func readInt64() int64 {
	nStr, e := reader.ReadString('\n')
	if e != nil {
		panic(e)
	}
	nStr = nStr[:len(nStr)-1]
	n, e := strconv.ParseInt(nStr, 10, 64)
	if e != nil {
		panic(e)
	}
	return n
}

func readInt64From(line string) int64 {
	n, e := strconv.ParseInt(line, 10, 64)
	if e != nil {
		panic(e)
	}
	return n
}

func readLineNumbs() []string {
	line, e := reader.ReadString('\n')
	if e != nil {
		panic(e)
	}
	line = line[:len(line)-1]
	numbs := strings.Split(line, " ")
	return numbs
}

func readArrInt() []int {
	numbs := readLineNumbs()
	arr := make([]int, len(numbs))
	for i, n := range numbs {
		val, e := strconv.Atoi(n)
		if e != nil {
			panic(e)
		}
		arr[i] = val
	}
	return arr
}

func readArrInt64() []int64 {
	numbs := readLineNumbs()
	arr := make([]int64, len(numbs))
	for i, n := range numbs {
		val, e := strconv.ParseInt(n, 10, 64)
		if e != nil {
			panic(e)
		}
		arr[i] = val
	}
	return arr
}

func readArrInt64From(numbs []string, start int) []int64 {
	arr := make([]int64, len(numbs)-start)
	for i, n := range numbs[start:] {
		val, e := strconv.ParseInt(n, 10, 64)
		if e != nil {
			panic(e)
		}
		arr[i] = val
	}
	return arr
}
