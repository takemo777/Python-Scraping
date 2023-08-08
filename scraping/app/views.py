from django.shortcuts import render
from .application import app
from .forms import Radio
import json

linkSet = None

def index(request):
    
    return render(request, 'index.html')

def choice(request):
    if request.method == 'GET':
        if 'input audio' in request.GET:
            global linkSet
            linkList = app.speechText()

    return render(request, 'choice.html', {'linkList': linkList, 'max' : len(linkList)})

def download(request):
    
    if request.method == 'POST':
        print(f'チェックされた値{request.POST.getlist("select")}')
        download_url = request.POST.getlist("select")
        app.startDownload(download_url)
        
    return render(request, 'end.html')
            
