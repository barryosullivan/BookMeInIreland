"""
***Website url's***
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #localhost:8000/BookMeInIreland
    url( r'^$', views.index, name='index' ),
]