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

	var hello string = "Hello World!"

	// Print out "Hello World" 10 times
	for i := 0; i < 10; i++ {
		fmt.Println(hello)
	}

}
