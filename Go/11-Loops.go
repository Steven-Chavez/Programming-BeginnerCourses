// Author: Steven Chavez
// FileName: 11-Loops.go
// Creation Date: 11/27/2022
//
// * The for loop is the only kind of loop available
// in go! *
//
// LOOP DEFINITION
// A loop itirates through a block of code a certian
// number of times
//
// FORMAT
// for statement1; statement2; statement3 {
//    // code to be executed for each iteration
// }
//
// EXAMPLE
// for i:=0; i < 5; i++ {
//    // code to be executed
// }
//
// STATEMENTS
// continue - Skip 1 loop iteration
// break - Stop the loop
// range - Used to iterate through an array

package main

import "fmt"

func main() {

	// Print out 1-10
	fmt.Println("----- 1-10 -----")
	for i := 0; i < 10; i++ {
		fmt.Println(i + 1)
	}

	// Print out evens from 1-20
	fmt.Println("----- 0-20 evens -----")
	for j := 0; j <= 20; j++ {
		var mod int = j % 2

		// logic to print our evens
		if mod != 0 {
			// used to skip a loop iteration
			continue
		}
		fmt.Println(j)
	}

	// Iterate through an array using range
	fmt.Println("----- a-e using range -----")
	letters := [5]string{"a", "b", "c", "d", "e"}
	for i, val := range letters {
		fmt.Println(i, "-", val)
	}

}
