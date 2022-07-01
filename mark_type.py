from Analytics import setup
setup()

from detect import is_question

import json
from main.models import Tweet
import re
from os import walk
filenames = next(walk("snsdata"), (None, None, []))[2] 
for files in filenames:
    # read file
    with open(f'snsdata/{files}', 'r') as loaded_data:
        data=loaded_data.read()
        data = json.loads(data)
    for d in data:
        #escape special characters from body with regex
        cleaned_body = re.sub(r'[^\w\s]','', d['body'])
        try:
            the_tweet = Tweet.objects.get(tweet_id=d['id'])
            if is_question(cleaned_body):
                the_tweet.is_question = True
                the_tweet.save()
                print(f'{d["id"]} is a question')
        except Tweet.DoesNotExist:
            print(f'{d["id"]} does not exist')
                
