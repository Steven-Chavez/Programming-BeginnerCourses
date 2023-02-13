// Author: Steven Chavez
// FileName: json.go
// Creation Date: 12/14/2022
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

type Person struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {
	//open file
	file, err := os.Open("C:\\Users\\Steven.Chavez\\go\\projects\\json\\MOCK_DATA.json")

	if err != nil {
		fmt.Println(err)
		return
	}

	defer file.Close()

	// Read file into a byte slice
	byteValue, _ := ioutil.ReadAll(file)

	// Unmarshal data into struct
	var user []Person
	err = json.Unmarshal(byteValue, &user)

	if err != nil {
		fmt.Println(err)
		return
	}

	// Print results
	fmt.Println(user)
}
