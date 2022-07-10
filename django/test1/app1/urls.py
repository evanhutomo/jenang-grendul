from django.urls import re_path
from app1 import views

urlpatterns = [
  re_path(r'^$', views.index, name='index'),
  re_path(r'^test1', views.test1, name='test1'),
  re_path(r'^help', views.help, name='help'),
  re_path(r'^show_django', views.show_django, name='show django'),
]

# this will become
# 127.0.0.1:5002/app1/ for index
# 127.0.0.1:5002/app1/test1 for test1
