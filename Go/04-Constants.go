// Author: Steven Chavez
// FileName: 04-Constants.go
// Creation Date: 11/23/2022
//
// FORMAT
// const CONSTNAME type = value
//
// DEF
// constants are variables that are unchangable
// and are read-only.
//
// RULES
// - Same naming convention as variables
// - Constant names are uppercase
// - Can be declared inside and outside of functions
// - There are two types of constants typed and untyped (inferred)
//

package main

import "fmt"

// Declaring a single constant
const HELLO string = "Hello World!"

// Declaring multiple constants
const (
	WORD         string  = "Apple"
	NUMBER       int     = 200
	DECIMEL      float32 = 2.35
	WORD_UNTYPED         = "Inferred"
)

func main() {
	fmt.Println(HELLO)
	fmt.Println(WORD, NUMBER, DECIMEL, WORD_UNTYPED)
}
