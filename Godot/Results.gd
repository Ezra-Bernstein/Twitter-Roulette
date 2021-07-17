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
	#print(get_tree().get_root().get_node("Main"))  #get_node("Main"))    # .get("GAME_CODE"))
	#http_request.request("http://localhost:5000/_getUsers?code=" + get_node("res://Results/Results").get("GAME_CODE"))

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
