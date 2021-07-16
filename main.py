from flask import Flask
from flask import render_template, request, session



app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/joinGame", methods=['POST'])
def joinGame():

    code = request.form['code']
    print(code)

    # if (gameExists(code)):
    return render_template('name.html')

@app.route("/name", methods=['POST'])
def name():

    username = request.form['username']

    #addUsertoGame(username)
    return render_template('game.html')

    
@app.route("/guess", methods=['POST'])
def guess():

    guess = request.form['guess']
    
    return render_template('game.html')

