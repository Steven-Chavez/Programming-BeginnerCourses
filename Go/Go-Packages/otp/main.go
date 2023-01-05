package main

import (
	"fmt"
	"time"

	"github.com/pquerna/otp/totp"
)

func main() {
	secret := "sdfhosdfoeinsdklfj"
	test, err := totp.GenerateCode(secret, time.Now())

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(test)
}
