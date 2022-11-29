// Author: Steven Chavez
// FileName: 10-Loops.go
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

package main

import "fmt"

func main() {

	// Print out 1-10
	fmt.Println("----- 1-10 -----")
	for i := 0; i < 10; i++ {
		fmt.Println(i + 1)
	}

	// Print out evens from 1-20
	fmt.Println("----- 1-20 evens -----")
	for j := 0; j < 20; j++ {
		var mod int
		mod = j % 2

		if mod == 0 {
			fmt.Println(j)
		} else {
			continue
		}
	}
}
