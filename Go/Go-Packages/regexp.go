// Author: Steven Chavez
// FileName: regexp.go
// Creation Date: 12/10/2022

package main

import (
	"fmt"
	"regexp"
)

func main() {
	musComp := regexp.MustCompile("\\d")

	ip := "10.0.0.0/2"

	output := musComp.FindString(ip)

	fmt.Println(output)

	found, err := regexp.MatchString("^[\\d]{1,3}\\.[\\d]{1,3}\\.[\\d]{1,3}\\.[\\d]{1,3}\\/[\\d]{1,2}$", ip)

	fmt.Println(found, err)
}
