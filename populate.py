from Analytics import setup

setup()

import json
from main.models import Tweet
import pandas as pd
from detect import is_question

def date_to_str(date):
    Date_Time = pd.to_datetime(date, unit='ms')
    return (str(Date_Time)[:10])

from os import walk
filenames = next(walk("others"), (None, None, []))[2] 

for files in filenames:
    # read file
    with open(f'others/{files}', 'r') as loaded_data:
        data=loaded_data.read()
        data = json.loads(data)
    for d in data:
        urls = d['url'].replace("\\", "")
        date = date_to_str(d['date'])
        is_a_question = is_question(d['body'])
        if not is_a_question:
            tweet = Tweet(tweet_id=d['id'], user_id=d['userid'], username=d['username'], url=urls, body=d['body'], date=date)
            tweet.is_others = True
            tweet.save()
    print(f'{files} is saved')
    