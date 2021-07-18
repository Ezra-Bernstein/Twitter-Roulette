extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var http_request = HTTPRequest.new()

# Called when the node enters the scene tree for the first time.
func _ready():
	add_child(http_request)
	http_request.connect("request_completed", self, "_on_request_completed")
	
	
	
	#get GAME_CODE from Main??
	print(Global.GAME_CODE)
	http_request.request("http://localhost:5000/_getUsers?code=" + Global.GAME_CODE)

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func _on_request_completed(result, response_code, headers, body):
	var responseText = body.get_string_from_utf8()
	var index = 0
	for i in responseText:
		if i =='(':
			responseText[index] = '['
		elif i == ')':
			responseText[index] = ']'
		index += 1
	
	print(responseText)
	print(JSON.parse(responseText))
	print(JSON.parse(responseText).result)
	print(JSON.parse(responseText).get_result())
	print(typeof(JSON.parse(responseText).result))
	
	
	var userList = JSON.parse(responseText).get_result()
	print(userList)
	for user in userList:
		$Scores.text += user[0] + " : " + user[7] + "\n"
	
	userList = JSON.parse(responseText).result
	print(userList)
	for user in userList:
		$Scores.text += user[0] + " : " + user[7] + "\n"
	
