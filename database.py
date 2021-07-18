import psycopg2
import os
from dotenv import load_dotenv
import random

load_dotenv()

CONNECTION_STRING = os.getenv('CONNECTION_STRING')

conn = psycopg2.connect(CONNECTION_STRING)

cur = conn.cursor()

def newGame(code):
    cur.execute("create table if not exists " + code + " (username STRING NOT NULL, vip BOOLEAN, guess1 STRING, \
        guess2 STRING, guess3 STRING, guess4 STRING, guess5 STRING, points INT)")
    conn.commit()

def gameExists(code):
    cur.execute("select exists (SELECT 1 AS result FROM pg_tables WHERE schemaname = 'public' AND tablename = %s)", (code,))
    exists = cur.fetchone()[0]
    return exists

def tableEmpty(code):
    cur.execute("select exists (SELECT 1 AS result FROM "+ code +")")
    exists = not cur.fetchone()[0]
    return exists

def addUserToGame(username, code):
    vip = tableEmpty(code)
    cur.execute("insert into "+ code +" values (%s, %s, default, default, default, default, default, %s)", (username, str(vip), str(0)))
    conn.commit()

def getUsers(code):
    cur.execute("select * from " + code)
    return cur.fetchall()

def getUser(code, username):
    cur.execute("select * from " + code + " where username = %s", (username,) )
    return cur.fetchone()

def getRandomUser(code):
    cur.execute("select username from " + code)
    users = cur.fetchall()
    user = users[random.randint(0, len(users) - 1)][0]
    return user

def setAnswer(code, round, answer):
    cur.execute("update "+code+" set guess"+str(round)+" = %s where guess"+str(round)+" is null", (answer,))
    conn.commit()

def getAnswer(code, round, username):
    print("getAnswer(): code: "+ code +" round: "+ str(round) +" username: "+ username )
    cur.execute("select guess"+str(round)+" from "+code+" where username=%s", (username,) )
    answer = cur.fetchone()[0]
    print("getAnswer(): answer: " + answer)
    return answer

def getPoints(code, username):
    cur.execute("select points from "+code+" where username=%s", (username,) )
    points = cur.fetchone()[0]
    return points

def getCurrentRound(code, username):
    print("getCurrentRound(): code: "+ code +" username: "+ username )
    cur.execute("select * from "+code)
    data = cur.fetchone()
    for i in range(2,8):
        print(i)
        if i == 7:
            return 5
        elif data[i] == None:
            print("getCurrentRound(): round: " + str(i-2))
            return i-2
        

def getNextNullRound(code, username):
    print("getNextNullRound(): code: "+ code +" username: "+ username )
    cur.execute("select * from "+code)
    data = cur.fetchone()
    for i in range(2,7):
        print(i)
        if i == 6:
            return 5
        elif data[i] == None:
            print("getNextNullRound(): round: " + str(i-1))
            return i-1


def checkGuess(code, round, username, answer):
    print("checkGuess(): code: "+ code +", round: "+ str(round) +", username: "+ username + ", answer: " + answer)
    
    currPoints = int(getPoints(code, username))
    print(currPoints)
    newPoints = str(currPoints + 100)

    print(getAnswer(code, round, username))
    print(answer)
    if (getAnswer(code, round, username) == answer):
        print("correct answer")
        cur.execute("update "+code+" set points=%s where username=%s", (newPoints, username,))
        conn.commit()
        return newPoints
    else:
        print("incorrect answer(?)")
    
    

#print(getUser('xbnkrp', 'joe'))

# print(getRandomUser('bddgbi'))
# setAnswer('phxdnj', 4, 'joe')
#print(getAnswer('jdddyk', 1, 'jack'))


#print(checkGuess('trnixi', 4, 'ezra_bernstein', 'bitplayer'))
# print(getPoints('phxdnj', 'bob'))
#print(getCurrentRound('phxdnj', 'bob'))


#print(getAnswer('arqlon', 1, 'jack'))

# print(getAnswer('arqlon', 3, 'jack'))
# print(checkGuess('arqlon', 1, 'jack', 'jack'))

# round = 1
# code = 'vhcago'
# username = 'ezra_bernstein'
# cur.execute("select guess"+str(round)+" from "+code+" where username=%s", (username,) )
# answer = cur.fetchone()[0]
# print(answer)