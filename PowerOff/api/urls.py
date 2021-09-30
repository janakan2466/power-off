from django.urls import path
from .views import main

#if the url's ending has /... then send that here
urlpatterns = [
    path('', main)
]