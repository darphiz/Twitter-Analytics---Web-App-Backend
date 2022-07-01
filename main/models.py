from django.db import models

class Thread(models.Model):
    tweet_id = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    body = models.TextField()
    url = models.URLField(max_length=250)
    date = models.DateField()
    
    def __str__(self):
        return self.tweet_id
    
    
class Tweet(models.Model):
    tweet_id = models.CharField(max_length=250)
    user_id = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    url = models.URLField(max_length=250)
    body = models.TextField()
    date = models.DateField()
    threads = models.ManyToManyField(Thread, related_name="replies")
    is_question = models.BooleanField(default=False)
    is_thread = models.BooleanField(default=False)
    is_fetched = models.BooleanField(default=False)
    is_others = models.BooleanField(default=False)
    def __str__(self):
        return self.tweet_id
        
    