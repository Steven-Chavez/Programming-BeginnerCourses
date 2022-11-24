// Author: Steven Chavez
// FileName: 05-Output.go
// Creation Date: 11/23/2022
//
// Go Output Functions
// - Print()
// - Println()
// - Printf()

package main

import "fmt"

var first, last string = "John", "Wick"

func main() {

	// Print()
	fmt.Print("----- Print() Output -----", "\n")
	// Print() has no formatting (newline, space, etc.)
	// unless the values are numeric then a space will
	// be added between
	fmt.Print(first)
	fmt.Print(last)

	// Print() with formatting
	fmt.Print("\n", first, " ", last, "\n")

	// Print() numeric example
	fmt.Print(1, 2, 3, 4, 5, "\n", "\n")

	// Println()
	fmt.Println("----- Println() Output -----")
	// Prints the first and last name on the same
	// with a space in between the first and last name
	fmt.Println(first, last)

	// Prints the first and last name on seperate lines
	fmt.Println(first)
	fmt.Println(last)
	fmt.Println()

	// Printf()
	fmt.Println("----- Printf() Output -----")

	// Prints out the value of the variable
	fmt.Printf("My first name is - %v", first)
	fmt.Println()
	fmt.Printf("My last name is - %v", last)

	// Prints out the type of the variable
	fmt.Println()
	fmt.Printf("The variable first is type - %T", first)
	fmt.Println()
	fmt.Printf("The variable last is type - %T", last)
	fmt.Println()
}
