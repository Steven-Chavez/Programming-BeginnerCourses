// Author: Steven Chavez
// FileName: 03-Variables.go
// Creation Date: 11/23/2022
//
// Variable Types
// int, float32, string, bool
//
// Variable Syntax
// var variable-name type = value
//
// Inferred Variable Syntax
// variable-name := value
//
// Difference between var and :=
// var - declaration and value assignment can be done seperatly
// := - used only in functions, value assignment and declaration
//      has to be done in the same line.

package main

import "fmt"

// variable declared outside of a function
var helloOutside = "Hello from the other side!"

func main() {
	// How to declare a variable using the var keyword
	var hello string = "Hello World!"
	fmt.Println(hello)

	// How to declare a vaiable using the inferred method
	helloInferred := "Hello World!"
	fmt.Println(helloInferred)

	// Declaring a variable without an initial value
	// will set the variable to it's default value.
	var helloDefault string
	fmt.Println(helloDefault) //Outpul will be blank ""

	// Populating a variable after delaration
	helloDefault = "Hello World!"
	fmt.Println(helloDefault)

	// Print variable outside of this function
	fmt.Println(helloOutside)
}
