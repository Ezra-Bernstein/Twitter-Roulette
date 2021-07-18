import requests
import os
from dotenv import load_dotenv
import random

load_dotenv()

BEARER=os.getenv('BEARER_TOKEN')


def getRandomTweet(username):
    r = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&exclude_replies=true&include_rts=false&tweet_mode=extended&since_id=1&count=3200", headers={'Authorization': 'Bearer '+BEARER})
    index = random.randint(0, len(r.json())-1)
    print(r.json()[index]['full_text'])
    return r.json()[index]['full_text']
