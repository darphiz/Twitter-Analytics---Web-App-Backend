from .serializers import TweetSerializers, ThreadSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from main.admin import Tweet 

@api_view(['GET'])
def get_thread_tweets(request):
    tweets_with_threads = Tweet.objects.filter(is_thread=True)
    serialized = TweetSerializers(tweets_with_threads, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_questions_tweets(request):
    tweets_with_question = Tweet.objects.filter(is_question=True)
    serialized = TweetSerializers(tweets_with_question, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_questions_tweets(request):
    tweets_with_question = Tweet.objects.filter(is_question=True)
    serialized = TweetSerializers(tweets_with_question, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_others(request):
    tweets_with_question = Tweet.objects.filter(is_others=True)
    serialized = TweetSerializers(tweets_with_question, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_thread_from_tweets(request):
    tweet_id = request.query_params.get('tweet_id')
    try:
        threads = Tweet.objects.filter(tweet_id=tweet_id)[0].threads.all()
    except Tweet.DoesNotExist:
        threads = None
    if threads:
        serialized = ThreadSerializers(threads, many=True)
        data = {
            "message": "ok",
            "thread" : serialized.data
        }
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({"message: ko"}, status=status.HTTP_200_OK)
    