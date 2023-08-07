
from django.contrib import admin
from django.urls import path
from app.views import index, choice

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('choice/', choice, name='choice'),
]
