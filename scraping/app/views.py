from django.shortcuts import render
from .application import app

def index(request):
    if request.method == 'GET':
        if 'input audio' in request.GET:
            listSet = app.speechText()
    return render(request, 'index.html')

def choice(request, listSet):
    
    return render(request, 'test.html', {'listSet': listSet})
