from django.shortcuts import render, HttpResponse

# Create your views here.
def index (request):
    return HttpResponse('helloo world<h1/>')

def my_url (reduest):
    return HttpResponse('my first page')