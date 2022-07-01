from Analytics import setup
setup()
from main.models import Tweet
from detect import is_question


tweets = Tweet.objects.filter(is_question=False, is_thread=False, is_others = False)
print(f"{len(tweets)} tweets to check")

for tweet in tweets:
    is_a_question = is_question(tweet.body)
    if not is_a_question:
        tweet.is_others = True
        tweet.save()
        print(f'{tweet.tweet_id} is others')
    else:
        tweet.delete()
        print(f'{tweet.tweet_id} is nothing')
     
