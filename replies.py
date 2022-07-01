from time import sleep
import pandas as pd
import snscrape.modules.twitter as sntwitter
import pandas as pd
import random

def next_day(date):
    date = str(date)
    last_two = int(date[-2:])
    if last_two < 28:
        new_last_two = int(last_two + 5)
        if new_last_two < 10:
            return str(date[:8]) + '0' + str(new_last_two)
        return str(date[:8]) + str(last_two + 5)
    else:
        middle = int(date[5:7])+1
        if middle < 10:
            return str(date[:5]) + '0' + str(middle) + '-01' 
        if middle > 12:
            front = int(date[:4]) + 1
            return str(front) + '-01-01'
        return str(date[:5]) + str(middle) + '-01'
    

    
    
def get_replies(tweet_id, date, username):
    tweet_date = date
    maximum_tweets = 1000
    replies= []
    # query = f"from:{username} to:{username} since:{tweet_date} until:{next_day(tweet_date)}"
    query = f"to:{username} since:{tweet_date} until:{next_day(tweet_date)}"
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i > maximum_tweets:
                break
        if str(tweet.inReplyToTweetId) == str(tweet_id):
        #uncomment for threads only  
        # if tweet.inReplyToTweetId == tweet_id or tweet.inReplyToUser.username == username:  
            replies.append([tweet.id, tweet.renderedContent, tweet.user.username, tweet.url, tweet.date])

    plotted_data = pd.DataFrame(replies, columns=['id', 'body', 'username', 'url', 'date'])
    return (plotted_data.sort_values('date').to_json(orient='records'))
