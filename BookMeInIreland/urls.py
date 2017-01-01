"""
* BookMeInIreland URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #localhost:8000/BookMeInIreland 
    url(r'^BookMeInIreland/', include('website.urls')),

    #localhost:8000/admin
    url(r'^admin/', include(admin.site.urls)),
]