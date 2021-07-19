extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var http_request = HTTPRequest.new()


# Called when the node enters the scene tree for the first time.
func _ready():
	$Timer_Label.hide()
	$Code.hide()
	add_child(http_request)
#	http_request.connect("request_completed", self, "_on_request_completed")
#	http_request.request(Global.url + "_getUser?code=bddgbi&username=bob")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	$Timer_Label.text = "Time left to join: " + str(round($Timer.time_left)) + " seconds"

func _on_Button_pressed():
	http_request.connect("request_completed", self, "_on_request_completed")
	http_request.request(Global.url + "_createGame")
	$Button.disabled = true

func _on_request_completed(result, response_code, headers, body):
	Global.GAME_CODE = body.get_string_from_utf8()
	print(Global.GAME_CODE)
	$Code.text = "Go to "+ Global.url + " and enter the game code below! \nGAME CODE: " + Global.GAME_CODE.to_upper()
	$Code.show()
	
	$Timer.wait_time = 60
	$Timer_Label.show()
	$Timer.start()


func _on_Timer_timeout():
	get_tree().change_scene("res://Question.tscn")
