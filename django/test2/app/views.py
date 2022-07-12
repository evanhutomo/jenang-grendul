from django.shortcuts import render

# Create your views here.
def index(request):
  d = { 'content': "the app" }
  return render(request, 'app/index.html', context=d)
