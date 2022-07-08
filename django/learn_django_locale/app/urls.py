#from django.conf.urls import url
from django.urls import re_path
from app import views

urlpatterns = [
    re_path('', views.indexx, name='indexx'),
]
