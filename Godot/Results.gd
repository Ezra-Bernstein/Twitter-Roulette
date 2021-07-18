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
	http_request.request(Global.url + "_getUsers?code=" + Global.GAME_CODE)

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
		elif i == '\'':
			responseText[index] = '"'
		index += 1
		
	if "True" in responseText:
		responseText = responseText.replace("True", "true")
	if "False" in responseText:
		responseText = responseText.replace("False", "false")
	
	print(responseText)
	
	print(str2var(responseText))
	var userList = str2var(responseText)
	for user in userList:
		$Scores.text += user[0] + " : " + str(user[7])+ "\n"
	
	
#	print(JSON.parse(responseText))
#	print(JSON.parse(responseText).result)
#	print(JSON.parse(responseText).get_result())
#	print(typeof(JSON.parse(responseText).result))
#
	
#	var userList = JSON.parse(responseText).get_result()
#	print(userList)
#	for user in userList:
#		$Scores.text += user[0] + " : " + user[7] + "\n"
#
#	userList = JSON.parse(responseText).result
#	print(userList)
#	for user in userList:
#		$Scores.text += user[0] + " : " + user[7] + "\n"
	
