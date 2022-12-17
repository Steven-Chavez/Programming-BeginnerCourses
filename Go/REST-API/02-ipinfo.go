//https://ipinfo.io/account/home
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strings"
	"json"
)

// Todo struct
type ipinfo struct {
	IP       string `json:"ip"`
	Hostname string `json:"hostname"`
	City     string `json:"city"`
	Region   string `json:"region"`
	Country  string `json:"country"`
	Loc      string `json:"loc"`
	Org      string `json:"org"`
	Postal   string `json:"postal"`
	Timezone string `json:"timezone"`
}

func get(ip string) {
	var err error
	var token []byte
	var url string
	var resp *http.Response

	token, err = os.ReadFile("/home/steven/api/ipinfo.txt")

	if err != nil {
		log.Fatalln(err)
	}

	url = "https://ipinfo.io/" + ip + "?token=" + string(token)
	url = strings.Replace(url, "\n", "", -1)

	resp, err = http.Get(url)

	if err != nil {
		log.Fatalln(err)
	}

	defer resp.Body.Close()
	bodyBytes, _ := ioutil.ReadAll(resp.Body)

	// Convert response body to string
	bodyString := string(bodyBytes)
	fmt.Println("API Response as String:\n" + bodyString)

	// Convert response body to Todo struct
	var todoStruct Todo
	json.Unmarshal(bodyBytes, &todoStruct)
	fmt.Printf("API Response as struct %+v\n", todoStruct)*/
	
	/*
		defer resp.Body.Close()
		bodyBytes, _ := ioutil.ReadAll(resp.Body)
		fmt.Println("1. Performing Http Get...")
		resp, err = http.Get("https://jsonplaceholder.typicode.com/todos/1")

		if err != nil {
			log.Fatalln(err)
		}

		defer resp.Body.Close()
		bodyBytes, _ := ioutil.ReadAll(resp.Body)

		// Convert response body to string
		bodyString := string(bodyBytes)
		fmt.Println("API Response as String:\n" + bodyString)

		// Convert response body to Todo struct
		var todoStruct Todo
		json.Unmarshal(bodyBytes, &todoStruct)
		fmt.Printf("API Response as struct %+v\n", todoStruct)*/
}

func main() {

	var ip string

	fmt.Print("Enter an IP: ")
	fmt.Scanln(&ip)
	get(ip)
}
