from flask import Flask
from flask import render_template, request, session
import random, string
from dotenv import load_dotenv
from database import *
from twitter import *
import jinja2

load_dotenv()

APP_SECRET_KEY=os.environ.get('APP_SECRET_KEY')

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #will be changed for production


@app.route("/")
def hello_world():
    session.clear()
    return render_template('home.html')

@app.route('/createGame', methods=['POST'])
def createGame():

    code = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(6))

    session['code'] = code
    newGame(code)
    

    return render_template('name.html')


@app.route("/joinGame", methods=['POST'])
def joinGame():

    code = request.form['code']
    code = code.lower()

    if (gameExists(code)):
        code = request.form['code']
        session['code'] = code
        return render_template('name.html')

    else:
        return render_template('home.html')

@app.route("/name", methods=['POST'])
def name():

    username = request.form['username']
    if checkUsername(username):
        session['username'] = username

        addUserToGame(username, session['code'])
        return render_template('start.html', user = getUser(session['code'], session['username']))
    else:
        return render_template('name.html')


@app.route('/start', methods=['POST'])
def start():
    print("game started!")
    return render_template('game.html', users=getUsers(session['code']), round = getCurrentRound(session['code'], session['username']))

    
@app.route("/guess", methods=['POST'])
def guess():

    #print(session['username'], session['code'])

    guess = request.form['guess']
    username = session['username']
    code = session['code']
    round = getCurrentRound(code, username)

    checkGuess(code, round, username, guess)
    if round == 5:
        return render_template('results.html')
    return render_template('game.html', users=getUsers(session['code']), round = getCurrentRound(session['code'], session['username']))

#client functions

@app.route('/_getUser', methods=['GET'])
def _getUser():
    code = request.args['code']
    username = request.args['username']

    return str(getUser(code, username))

@app.route('/_createGame', methods=['GET'])
def _createGame():
    code = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(6))
    newGame(code)
    return code

@app.route('/_getUsers', methods=['GET'])
def _getUsers():
    code = request.args['code']

    return str(getUsers(code))

@app.route('/_getTweet', methods=['GET'])
def _getTweet():

    code = request.args['code']
    
    username = getRandomUser(code)
    round = getNextNullRound(code, username)

    setAnswer(code, round, username)

    return getRandomTweet(username)




if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)
