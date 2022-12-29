package main

import (
	"fmt"
	"os"
	"time"
)

func main() {

	now := time.Now()
	s := now.Format("2006-01-02 15:04:05")

	filename := "/tmp/" + "test_" + s

	file, err := os.OpenFile(filename, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0644)

	if err != nil {
		fmt.Println(err)
		return
	}

	file.Close()

}
