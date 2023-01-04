package main

import (
	"custompackage/mypackage"
	"fmt"
)

func main() {
	output := mypackage.HelloWorld()
	fmt.Println(output)
}
