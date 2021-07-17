extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var http_request = HTTPRequest.new()
var GAME_CODE


# Called when the node enters the scene tree for the first time.
func _ready():
	
	add_child(http_request)
#	http_request.connect("request_completed", self, "_on_request_completed")
#	http_request.request("http://localhost:5000/_getUser?code=bddgbi&username=bob")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass;

func _on_Button_pressed():
	http_request.connect("request_completed", self, "_on_request_completed")
	http_request.request("http://localhost:5000/_createGame")
	$Button.disabled = true


func _on_request_completed(result, response_code, headers, body):
	GAME_CODE = body.get_string_from_utf8()
	print(GAME_CODE)
	$Label.text = "GAME CODE: " + GAME_CODE
	
	$Timer.wait_time = 5
	$Timer.start()
	
	

#func _on_request_completed(result, response_code, headers, body):
#	var json = JSON.parse(body.get_string_from_utf8())
#	print(json.result)
#	self.text = str(json.result)


func _on_Timer_timeout():
	get_tree().change_scene("res://Question.tscn")
