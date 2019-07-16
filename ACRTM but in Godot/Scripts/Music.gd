extends Node

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	print("Ready Music")
	reset_timer()
	
func reset_timer():
	var time_till_stop = 3600 - (OS.get_time().values()[1] * 60 + OS.get_time().values()[2])
	$MusicCheck.wait_time = time_till_stop
	$MusicCheck.start()

func _on_MusicCheck_timeout():
	reset_timer()