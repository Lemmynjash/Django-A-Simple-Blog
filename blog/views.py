from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [

    {
        'author': 'Heeey1',
        'title': 'My heey title',
        'content': "First post content",
        'date': '2019-10-10'
    },
    {
        'author': 'Heeey2',
        'title': 'My heey title',
        'content': 'First post content',
        'date': '2019-10-10'
    }
]


def home(request):
    context = {
        'posts': posts
    }

    context2 = {
        'poststwo': posts
    }

    return render(request, 'blog/home.html', context, context2)


def about(request):
    return render(request, 'blog/about.html', {'title': 'AboutMEEEEEE',
                                               'poststhree': 'heeeey',
                                               'poststwo': posts})
