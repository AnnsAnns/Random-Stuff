package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"strings"
	"time"

	"fyne.io/fyne"

	"fyne.io/fyne/widget"
)

type contractKills struct {
	objectiveClass  string
	objectiveWeapon string
	objectiveKills  int16
}

type Gametracker struct {
	playerName string
	playerTeam string

	contract contractKills

	objectiveKillsCurrent int16

	isContractFinished bool

	confTF2Gamepath string

	uiObjectiveTitle string
	uiTitle          string

	mApp    fyne.App
	mWindow fyne.Window
}

func (gt *Gametracker) parseConsole() {
	gt.consoleExec("condump")
	time.Sleep(time.Second)

	file, err := os.Open(gt.confTF2Gamepath + `\tf\condump000.txt`)
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if strings.HasPrefix(line, gt.playerName) {
			if strings.Contains(line, gt.contract.objectiveWeapon) {
				gt.objectiveKillsCurrent++
			}
		}
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	file.Close()
	os.Remove(gt.confTF2Gamepath + `\tf\condump000.txt`)
}

func (gt *Gametracker) cleanConsole() {
	gt.consoleExec("clear")
}

func (gt *Gametracker) checkObjectives() {
	if gt.contract.objectiveKills <= gt.objectiveKillsCurrent {
		gt.isContractFinished = true
		fmt.Println("Congrats, you finished your contract.")
	}
}

func (gt *Gametracker) getNewContract() {
	// @TODO: Actually implement more contracts

	gt.contract = contractKills{"Scout", "scattergun", 5}
}

func (gt *Gametracker) consoleExec(arg string) {
	arg = "-hijack \"+" + arg + "\""

	fmt.Println(arg)

	cmd := exec.Command("./hl2.exe", arg)
	cmd.Dir = gt.confTF2Gamepath
	cmd.Run()

	fmt.Println(cmd.String())
}

func (gt *Gametracker) guiInit() {
	// @TODO: Actually implement a GUI

	gt.mWindow.SetContent(widget.NewLabel("TF2 Contracts Test v0.0.1 \n"))

	gt.mWindow.ShowAndRun()
	gt.parseConsole()
}

func (gt *Gametracker) init() {
	fmt.Println("Please supply your Username and Gamepath via the env vars TF2_GAMEPATH and TF2_USERNAME")

	gt.confTF2Gamepath = os.Getenv("TF2_GAMEPATH")
	if gt.confTF2Gamepath == "" { // Default to this
		gt.confTF2Gamepath = `T:\SteamApp\steamapps\common\Team Fortress 2`
	}

	gt.playerName = os.Getenv("TF2_USERNAME")

	gt.consoleExec("log_verbose_enable 1")
}

func main() {
	var gt Gametracker

	gt.init()

	for {
		if gt.isContractFinished {
			gt.getNewContract()
		}

		gt.parseConsole()
		gt.cleanConsole()
		gt.checkObjectives()

		time.Sleep(time.Second * 3)
	}
}
