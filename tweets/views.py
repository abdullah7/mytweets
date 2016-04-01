from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from user_profile.models import User
from tweets.models import Tweet, HashTag
from forms import TweetForm

class Index(View):
    """
    Index template view
    """
    def get(self, request):
        params = {}
        params["name"] = "ABD"

        return render(request, 'base.html', params)


class Profile(View):
    """
    User Profile page reachable from /user/<username> URL
    """
    def get(self, request, username):
        params = dict()
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        params["tweets"] = tweets
        params["user"] = user
        params["form"] = TweetForm()
        return render(request, 'profile.html', params)


class PostTweet(View):
    """
    Tweet Post form available on page /user/<username> URL
    """
    def post(self, request, username):
        form = TweetForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=username)
            tweet = Tweet(text=form.cleaned_data['text'],
                user=user,
                country=form.cleaned_data['country'])
            tweet.save()

            words = form.cleaned_data['text'].split(" ")
            for word in words:
                if word[0] == "#":
                    hashtag, created = HashTag.objects.get_or_create(name=word[1:])
                    hashtag.tweet.add(tweet)

        return HttpResponseRedirect('/user/' + username)


class HashTagCloud(View):
    """
    Hash Tag page reachable from /hashtag/<hashtag> URL
    """
    def get(self, request, hashtag):
        params = dict()
        obj = HashTag.objects.get(name=hashtag)
        params["tweets"] = obj.tweet.all
        return render(request, 'hashtag.html', params)

