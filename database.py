import psycopg2
import os
from dotenv import load_dotenv

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
    cur.execute("insert into "+ code +" values (%s, %s, %s, %s)", (username, str(vip), "", str(0)))
    conn.commit()

def getUsers(code):
    cur.execute("select * from " + code)
    return cur.fetchall()

def getUser(code, username):
    cur.execute("select * from " + code + " where username = %s", (username,) )
    return cur.fetchone()

#print(getUser('xbnkrp', 'joe'))