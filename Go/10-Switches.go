// Author: Steven Chavez
// FileName: 10-Switches.go
// Creation Date: 11/28/2022
//
// SWITCH DEF
// Runs blocks of code based on matched values
//
// FORMAT
// switch variable_with_data_you_want_to_compare {
// case x:
//    // code block
// case y:
//    // code block
// case z:
// ...
// default: // Optional - Used if no case matches
//    // code block
// }

package main

import "fmt"

func main() {

	// variables
	var i int
	var modulas int

	// Print out directions
	fmt.Print("\n", "Enter a number to see if it's even or odd: ")

	// Read user input
	fmt.Scanln(&i)

	// If modulas equals zero the number is even
	modulas = i % 2

	// Switch statment
	switch modulas {
	case 0:
		fmt.Println(i, "- is even")
	default:
		fmt.Println(i, "- is odd")

	}
}
