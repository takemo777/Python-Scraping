from django.shortcuts import render
from .application import app
from .forms import Radio
import json

def index(request):
    
    return render(request, 'index.html')

def viewAcquisitionSound(request):
    
    return render(request, )

def choice(request):
    if request.method == 'GET':
        if 'output audio' in request.GET:
            
            keyword = request.GET['keyword'] #index.htmlのinput要素からkeywordを取得
            print(keyword)
            linkList = app.speechText(keyword)

    return render(request, 'choice.html', {'linkList': linkList, 'max' : len(linkList)})

def download(request):
    
    if request.method == 'POST':
        print(f'チェックされた値{request.POST.getlist("select")}')
        download_url = request.POST.getlist("select")
        app.startDownload(download_url)
        
    return render(request, 'end.html')
            
