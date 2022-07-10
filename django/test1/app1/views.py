from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError

def index(request):
  d = {
    'insert_me': "this from views.py",
    'the_index': "the value"
    }
  return render(request, 't1.html', context=d)

def help(request):
  d = {
    'help_msg': "the value of help page"
    }
  return render(request, 'app1/help.html', context=d)

def test1(request):
  return HttpResponse("test1!")

def show_django(request):
  d = {
    'django_msg': "the value of show_django.html"
    }
  return render(request, 'app1/show_django.html', context=d)
