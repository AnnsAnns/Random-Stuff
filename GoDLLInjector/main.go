package main

import "C"
import "os"

//export testFunction
func testFunction() {
	println("Hello from gOwO")

	os.Create("FileFromDLLProcess.pog")
}

func main() {
	testFunction()
}
