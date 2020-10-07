package main

import (
	"fmt"

	"github.com/librespot-org/librespot-golang/librespot"
)

func main() {
	fmt.Println("Connecting")

	conn, err := librespot.Login("USERNAME", "PASSWORD", "Test Device 1")
	if err != nil {
		fmt.Print("Oh no")
		panic(err)
	}

	fmt.Println(conn.Username())
	track, err := conn.Mercury().GetTrack("1dHBD95TLrBX3Z6x2SnMs5")

	if err != nil {
		panic(err)
	}

	fmt.Println(track.Name)
	conn.Player().LoadTrack(audio, track.Gid)
}
