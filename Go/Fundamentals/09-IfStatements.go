// Author: Steven Chavez
// FileName: 09-IfStatements.go
// Creation Date: 11/30/2022
//
// IF STATEMENT DEFINITION
// Executes a block of code if a condition is met.
//
// SYNTAX
// if condition {
// 	// code to be executed
// } else if condition2 {
// 	// code to be executed
// } else {
// 	// code to be executed if no condition is met
// }

package main

import "fmt"

func main() {
	// variable
	var input string

	// print out menu
	fmt.Print("\n", "Are you a robot (Y/N)? ")
	fmt.Scanln(&input)

	if input == "Y" {
		fmt.Println("No robots allowed!!")
	} else if input == "N" {
		fmt.Println("You are allowed!!")
	} else {
		fmt.Println("Invalid input, goodbye!")
	}

}
