// Author: Steven Chavez
// FileName: 07-Slices.go
// Creation Date: 11/26/2022
//
// SLICE DEF
// Used to store multiple variables. Like an array
// but it's lenth can grow and shrink
//
// FORMAT
// slice_name := []datatype{values}
//
// EXAMPLE
// myslice := []int{}

package main

import "fmt"

func main() {
	// Initiate an empty slice
	slice_numbers := []int{}
	fmt.Println(slice_numbers)

	// Append data to empty slice
	slice_numbers = append(slice_numbers, 10, 20, 30, 40, 50)
	fmt.Println(slice_numbers)

	// Print out the length and capacity of slice
	fmt.Println("Lenth:", len(slice_numbers))
	fmt.Println("Capacity:", cap(slice_numbers))
}
