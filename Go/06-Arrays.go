// Author: Steven Chavez
// FileName: 06-Arrays.go
// Creation Date: 11/26/2022

package main

import "fmt"

var array_defined = [3]string{"Hello", " ", "World!"}
var array_inferred = [...]string{"Hello", " ", "World!"}

func main() {
	// Print out full arrays
	fmt.Println(array_defined)
	fmt.Println(array_inferred)

	// Print out each entry element in array
	fmt.Print(array_defined[0], array_defined[1], array_defined[2])
	fmt.Print("\n", array_inferred[0], array_inferred[1], array_inferred[2], "\n")

	// Modify an element in an array
	array_defined[0] = "Goodbye"
	fmt.Print(array_defined[0], array_defined[1], array_defined[2], "\n")

	// Initilaze specific array elements
	var array_specific = [5]int{0: 10, 4: 50}
	fmt.Println(array_specific)

	// Find the length of an array
	fmt.Println("Array Lenth:", len(array_specific))
}
