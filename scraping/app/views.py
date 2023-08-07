from django.shortcuts import render
from .application import app
from .forms import Radio

listSet = None

def index(request):
    
    return render(request, 'index.html')

def choice(request):
    if request.method == 'GET':
        if 'input audio' in request.GET:
            global listSet
            listSet = app.speechText()
    return render(request, 'choice.html', {'listSet': listSet, 'max' : len(listSet)})

def download(request):
    
    if request.method == 'POST':
        max = int(request.POST["max"])
        app.startDownload(listSet, max)
        
    return render(request, 'end.html')
            
