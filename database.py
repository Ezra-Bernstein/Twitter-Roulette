import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv('CONNECTION_STRING')

conn = psycopg2.connect(CONNECTION_STRING)

cur = conn.cursor()

def newGame(code):
    cur.execute("create table if not exists " + code + " (username STRING NOT NULL, vip BOOLEAN, guess STRING, points INT)")
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
    vip = not tableEmpty(code)
    cur.execute("insert into "+ code +" values (%s, %s, %s, %s)", (username, str(vip), "", str(0)))
    conn.commit()

# def checkGuess():

# newGame('asdf')
# print (gameExists('asdf'))
# print (tableEmpty('asdf'))
# addUserToGame('username', 'asdf')
# print (tableEmpty('asdf'))
