from pyexpat import model
from main.models import Tweet, Thread
from rest_framework import serializers

class TweetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
        
class ThreadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'