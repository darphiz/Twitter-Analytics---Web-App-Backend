from django.contrib import admin
from .models import Thread, Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ('tweet_id', 'username', 'is_question', 'url')
    search_fields = ('tweet_id', 'username', 'body')
    
admin.site.register(Thread)
admin.site.register(Tweet, TweetAdmin)
