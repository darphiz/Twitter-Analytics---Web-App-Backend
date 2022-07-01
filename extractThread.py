from Analytics import setup
setup()
from replies import get_replies
from main.models import Tweet, Thread
import json
import pandas as pd

def date_to_str(date):
    Date_Time = pd.to_datetime(date, unit='ms')
    return (str(Date_Time)[:10])

all_tweets = Tweet.objects.filter(is_question=True)
print(f"{len(all_tweets)} tweets detected")
counting = len(all_tweets)
for tweet in all_tweets:
    print(f'working on {tweet.tweet_id}')
    print(f'{counting} tweets left')
    threads = get_replies(tweet.tweet_id, tweet.date, tweet.username)
    all_thread = json.loads(threads)
    try:
        if all_thread:
            for thread in all_thread:
                load_tweet = Tweet.objects.get(tweet_id=tweet.tweet_id)
                date = date_to_str(thread['date'])
                thread_obj = Thread.objects.create(tweet_id=thread['id'], username=thread['username'], body=thread['body'], url=thread['url'], date=date)
                load_tweet.threads.add(thread_obj)
                # load_tweet.is_thread = True
                load_tweet.save()
                print(f"{load_tweet.tweet_id} thread saved")
        else:
            print(f'{tweet.tweet_id} has no thread')
        load_tweet = Tweet.objects.get(tweet_id=tweet.tweet_id)
        load_tweet.is_fetched = True
        load_tweet.save()
    except Tweet.DoesNotExist:
        print(f'{tweet.tweet_id} does not exists')        

    counting -= 1
    
