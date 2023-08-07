from django.contrib import admin
from django.urls import path
from app.views import index, choice, download

app_name = 'app'
urlpatterns = [
    path('choice/', choice, name='choice'),
    path('', index, name='index'),
    path('download/', download, name='download'),
]