extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var counter = 1
var http_request = HTTPRequest.new()
var question


# Called when the node enters the scene tree for the first time.
func _ready():
	add_child(http_request)
	http_request.connect("request_completed", self, "_on_request_completed")
	http_request.request("http://localhost:5000/_getTweet?code=" + Global.GAME_CODE)
	$Timer.wait_time = 10
	


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	$Timer_Label.text = "Time left to answer: " + str(round($Timer.time_left)) + " seconds"

func _on_request_completed(result, response_code, headers, body):
	question = str(body.get_string_from_utf8())
	print("QUESTION " + question)
	$Question_Label.text = "“" + question + "”"
	$Timer.start()
	counter += 1
	$Round_Label.text = "ROUND " + str(counter-1)
	
func _on_Timer_timeout():
	if counter < 6:
		$Timer.wait_time = 10
		http_request.request("http://localhost:5000/_getTweet?code=" + Global.GAME_CODE)
		
	else:
		$Timer.wait_time = 0
		$Timer.stop()
		$Timer_Label.text = "Time left to answer: " + str(round($Timer.time_left)) + " seconds"
		$Question_Label.text = "GAME OVER"
		get_tree().change_scene("res://Results.tscn")
		
