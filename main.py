from flask import Flask
from flask import render_template, request, session
import random, string
from database import *


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #will be changed for production


@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/createGame', methods=['POST'])
def createGame():

    code = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(6))
    print (code)
    #newGame(code)


@app.route("/joinGame", methods=['POST'])
def joinGame():

    code = request.form['code']
    session['code'] = code
    print(code)

    # if (gameExists(code)):
    return render_template('name.html')

@app.route("/name", methods=['POST'])
def name():

    username = request.form['username']
    session['username'] = username

    #addUserToGame(session['code'], username)
    return render_template('game.html')

    
@app.route("/guess", methods=['POST'])
def guess():

    #print(session['username'], session['code'])

    guess = request.form['guess']
    
    #checkGuess()
    return render_template('game.html')
