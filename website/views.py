"""
***Website Views***
"""
from django.shortcuts import render, HttpResponse

#Index Page for the website
def index( request ):
    context = {
    'head_title': 'Book Me In Ireland',
    }
    return render( request, 'website/index.html', context )