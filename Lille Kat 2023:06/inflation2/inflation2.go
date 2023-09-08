package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// 28/88 accepted cases, should use a tree structure instead to store the prices and amounts.
// Should pull the nodes from the tree when needing to update the prices, and reinsert them with new prices

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
		ws.WriteString(fmt.Sprintf("Updating node with price %d. Amount before: %d, amount after: %d. Amount added: %d\n", newNode.price, root.amount, root.amount+newNode.amount, newNode.amount))
		root.amount += newNode.amount
	}
}

func (t *BinaryTree) Remove(price int64) *node {
	if t.root == nil {
		return nil
	}

	var parent *node
	current := t.root
	for current != nil {
		if price < current.price {
			parent = current
			current = current.left
		} else if price > current.price {
			parent = current
			current = current.right
		} else {
			break
		}
	}

	if current == nil {
		return nil // Node with the given price not found
	}

	if current.left == nil && current.right == nil {
		// Case 1: Node is a leaf node
		if parent == nil {
			t.root = nil
		} else if parent.left == current {
			parent.left = nil
		} else {
			parent.right = nil
		}
	} else if current.left == nil {
		// Case 2: Node has only a right child
		if parent == nil {
			t.root = current.right
		} else if parent.left == current {
			parent.left = current.right
		} else {
			parent.right = current.right
		}
	} else if current.right == nil {
		// Case 3: Node has only a left child
		if parent == nil {
			t.root = current.left
		} else if parent.left == current {
			parent.left = current.left
		} else {
			parent.right = current.left
		}
	} else {
		// Case 4: Node has both left and right children
		successor := t.findMinimum(current.right)
		current.price = successor.price
		current.amount = successor.amount
		current.right = t.removeNode(current.right, successor.price)
	}

	return current
}

func (t *BinaryTree) removeNode(root *node, price int64) *node {
	if root == nil {
		return nil
	}

	if price < root.price {
		root.left = t.removeNode(root.left, price)
	} else if price > root.price {
		root.right = t.removeNode(root.right, price)
	} else {
		if root.left == nil && root.right == nil {
			root = nil
		} else if root.left == nil {
			root = root.right
		} else if root.right == nil {
			root = root.left
		} else {
			successor := t.findMinimum(root.right)
			root.price = successor.price
			root.amount = successor.amount
			root.right = t.removeNode(root.right, successor.price)
		}
	}

	return root
}

func (t *BinaryTree) findMinimum(root *node) *node {
	if root.left == nil {
		return root
	}
	return t.findMinimum(root.left)
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
	ws.WriteString("(Price: " + strconv.FormatInt(globalInflation+root.price, 10) + ", Amount: " + strconv.FormatInt(root.amount, 10) + ")")

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

	ws.WriteString(fmt.Sprintf("(%d + %d) * %d = %d\n", root.price, globalInflation, root.amount, sum))

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

		tree.Print()
		ws.WriteString(fmt.Sprint(line, "\n"))

		if line[0] == 'I' {
			fmt.Sscanf(line, "INFLATION %d", &inflation)

			globalInflation += inflation
		} else {
			fmt.Sscanf(line, "SET %d %d", &x, &y)

			if x != y {
				removedNode := tree.Remove(x - globalInflation)
				if removedNode != nil {
					tree.Insert(y-globalInflation, removedNode.amount)
					// This is bad:
					// tree.insertNode(tree.root, removedNode)
				}
			}
		}

		tree.Print()

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
