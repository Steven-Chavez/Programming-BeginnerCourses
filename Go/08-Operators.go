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

	//-------------------------------
	// ARITHMETIC OPERATORS
	// Used to perform math operations
	//
	// +  Addition
	// -  Subtraction
	// *  Multiplcation
	// /  Division
	// %  Modulas
	// ++ Increment
	// -- Decrement

	fmt.Println(a + a)
	fmt.Println((c + c) / 10)
	fmt.Println(a * b)

	//------------------------------
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
	// Setting variable back to original value
	a = 10

	//------------------------------
	// COMPARISON OPERATORS
	// Used to compare two variables
	//
	// The return value is either true(1) or false(0)
	//
	// == Equals to "Are they the same"
	// != Not equal
	// >  Greater than
	// <  Less than
	// >= Greater than or equal to
	// <= Less than or equal to

	fmt.Println(a == b) //0 - False
	fmt.Println(a != b) //1 - True

	//-------------------------------
	// LOGICAL OPERATORS
	// Used to determine the logic between values
	//
	// && Logical AND
	// || Logical OR
	// !  Logical NOT

	// Requires both sides to be true
	fmt.Println(a == 20 && a == 10) // false

	// Either side needs to be true
	fmt.Println(a == 20 || a == 10) // true
}
