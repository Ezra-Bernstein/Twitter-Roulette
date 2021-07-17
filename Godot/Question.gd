extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var counter = 1


# Called when the node enters the scene tree for the first time.
func _ready():
	$Timer.wait_time = 10
	$Timer.start()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	$Timer_Label.text = str($Timer.time_left)


func _on_Timer_timeout():
	if counter < 6:
		$Timer.wait_time = 10
		$Timer.start()
		$Label.text = $Label.text + "AAA"
		counter += 1
		$Round_Label.text = "ROUND " + str(counter)
	else:
		$Timer.wait_time = 0
		$Timer.stop()
		$Timer_Label.text = str($Timer.time_left)
		$Label.text = "GAME OVER"
		get_tree().change_scene("res://Results.tscn")
		
