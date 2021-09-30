from django.shortcuts import render
from django.http import HttpResponse
# Create your apiendpoints here.
# Endpoint is a location on a server you are going to

def main(request):
    #endpoint retunrs response ex. json, html etc.
    return HttpResponse("<h1>Hello</h1>")
    