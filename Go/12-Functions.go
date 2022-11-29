// Author: Steven Chavez
// FileName: 12-Functions.go
// Creation Date: 11/27/2022
//
// FUNCTION DEFINITION
// Block of code that can be used repeatedly throughout
// your code
//
// FORMAT
//
// func FunctionName(param type, param type, ..){
//	// code
//	return output
// }
//

package main

import "fmt"

// Basic function
func helloWorld() {
	var hw string = "Hello World!"
	fmt.Println(hw)
}

// Function with parameters
func addNumbers(a int, b int) {
	fmt.Println(a + b)
}

// Function with parameters and return
func multiplyNumbers(a int, b int) int {
	return a * b
}

// Function with parameters and named return
func divideNumbers(a int, b int) (results int) {
	results = a / b
	return
}

func main() {
	// call helloWorld()
	helloWorld() // calls the function
	helloWorld()
	helloWorld()

	// call addNumbers()
	addNumbers(6, 23)
	addNumbers(20, 20)
	addNumbers(13, 78)

	// call multiplyNumbers()
	result := multiplyNumbers(5, 4)
	fmt.Println(result)

	// call divideNumbers()
	result = divideNumbers(1000, 34)
	fmt.Println(result)
}
