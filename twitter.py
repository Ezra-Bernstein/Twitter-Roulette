import requests
import os
from dotenv import load_dotenv
import random

load_dotenv()

BEARER=os.getenv('BEARER_TOKEN')

r = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=jack&exclude_replies=true&include_rts=false&tweet_mode=extended&since_id=1&count=3200", headers={'Authorization': 'Bearer '+BEARER})

#print(r.json())
print(len(r.json()))

# for tweet in r.json():
#     print(tweet['full_text'] + "\n")

index = random.randint(0, len(r.json()))
print(r.json()[index]['full_text'])