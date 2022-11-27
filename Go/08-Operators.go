// Author: Steven Chavez
// FileName: 08-Operators.go
// Creation Date: 11/27/2022
//
// OPERATORS DEF
// Used to perform operations on variables and values
// like math, comparing, equals to, ect

package main

import "fmt"

func main() {
	// Variables
	var a int = 10
	var b int = 50
	var c int = 100

	// ARITHMETIC OPERATORS
	// Used to perform math operations
	//
	// + Addition
	// - Subtraction
	// * Multiplcation
	// / Division
	// % Modulas
	// ++ Increment
	// -- Decrement

	fmt.Println(a + a)
	fmt.Println((c + c) / 10)
	fmt.Println(a * b)

	// ASSIGNMENT OPERATORS
	// Used to assign values to variables
	//
	// = Assigns value to variable
	// +=, -=, *=, /=, %=, &=, |=, ^=, >>=, <<=

	// Same as a = a + 10
	a += 10
	fmt.Println(a) // 20

	// Same as a = a % 10
	a %= 2
	fmt.Println(a) // 0

}
