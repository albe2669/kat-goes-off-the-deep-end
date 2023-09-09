package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// 28/88 accepted cases, this is too slow

var reader = bufio.NewReader(os.Stdin)
var ws = bufio.NewWriter(os.Stdout)
var globalInflation int64 = 0

type node struct {
	price  int64
	amount int64
	left   *node
	right  *node
}

type BinaryTree struct {
	root *node
}

func NewBinaryTree() *BinaryTree {
	return &BinaryTree{}
}

func (t *BinaryTree) Insert(price int64, amount int64) {
	newNode := &node{
		price:  price,
		amount: amount,
	}

	if t.root == nil {
		t.root = newNode
	} else {
		t.insertNode(t.root, newNode)
	}
}

func (t *BinaryTree) Set(x, y int64) {
	t.setNode(t.root, x, y)
}

func (t *BinaryTree) setNode(head *node, x, y int64) {
	if head == nil {
		return
	}

	// Recursively traverse the tree
	// Check if the current node's value is x
	if head.price == x {
		// Transfer the amount to the node with value y
		// ws.WriteString("setNode found x\n")
		t.Insert(y, head.amount)
		head.amount = 0
		return
	}

	t.setNode(head.left, x, y)
	t.setNode(head.right, x, y)
}

func (t *BinaryTree) insertNode(root *node, newNode *node) {
	if newNode.price < root.price {
		if root.left == nil {
			root.left = newNode
		} else {
			t.insertNode(root.left, newNode)
		}
	} else if newNode.price > root.price {
		if root.right == nil {
			root.right = newNode
		} else {
			t.insertNode(root.right, newNode)
		}
	} else {
		// If a node with the same price already exists, update its amount
		// ws.WriteString(fmt.Sprintf("Updating node with price %d. Amount before: %d, amount after: %d. Amount added: %d\n", newNode.price, root.amount, root.amount+newNode.amount, newNode.amount))
		root.amount += newNode.amount
	}
}

func (t *BinaryTree) Print() {
	t.printNode(t.root)
	ws.WriteString("\n")
}

func (t *BinaryTree) printNode(root *node) {
	if root == nil {
		return
	}

	t.printNode(root.left)

	// Print the node's price and amount
	// ws.WriteString("(Price: " + strconv.FormatInt(globalInflation+root.price, 10) + ", Amount: " + strconv.FormatInt(root.amount, 10) + ")")

	t.printNode(root.right)
}

func (t *BinaryTree) Sum(globalInflation int64) int64 {
	return t.sumNode(t.root, globalInflation)
}

func (t *BinaryTree) sumNode(root *node, globalInflation int64) int64 {
	if root == nil {
		return 0
	}

	sum := (root.price + globalInflation) * root.amount
	sum += t.sumNode(root.left, globalInflation)
	sum += t.sumNode(root.right, globalInflation)

	return sum
}

func main() {

	tree := NewBinaryTree()

	n := readInt()
	for i := 0; i < n; i++ {
		price := int64(readInt())
		tree.Insert(price, 1)
	}

	days := readInt()
	var inflation int64
	var x, y int64

	for i := 0; i < days; i++ {
		line := readLine()

		//tree.Print()
		// ws.WriteString(fmt.Sprint(line, "\n"))

		if line[0] == 'I' {
			fmt.Sscanf(line, "INFLATION %d", &inflation)

			globalInflation += inflation
		} else {
			fmt.Sscanf(line, "SET %d %d", &x, &y)

			if x != y {
				tree.Set(x-globalInflation, y-globalInflation)
			}
		}

		// tree.Print()

		ws.WriteString(fmt.Sprint(tree.Sum(globalInflation)) + "\n")
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

// readInt reads a single int from stdin
func readInt() int {
	var x int
	fmt.Scan(&x)
	return x
}

// readInts reads a line of space-separated ints from stdin
func readInts() []int {
	line := readLine()
	var xs []int

	for _, num := range strings.Split(line, " ") {
		n, err := strconv.Atoi(num)
		if err != nil {
			panic(err)
		}
		xs = append(xs, n)
	}

	return xs
}
