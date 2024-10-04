from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Tweet
# Create your views here.


def home_view(request):
    return HttpResponse("<h1>Hello World</h1>")


def tweet_detail_view(request, tweet_id):
    try:
        obj = Tweet.objects.get(id=tweet_id)
        return HttpResponse(f"<h1>{tweet_id}</h1><p>{obj.content}</p>")
    except:
        raise Http404("Page Not Found")
