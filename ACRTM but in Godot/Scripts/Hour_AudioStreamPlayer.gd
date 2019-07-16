extends AudioStreamPlayer

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	change_music()

func change_music():
	
	if playing:
		
		stop()
	var sfx = load("res://Audio/" + str(OS.get_time().values()[0]) + ".ogg")
	stream = sfx
	play()

func _on_MusicCheck_timeout():
	change_music()
