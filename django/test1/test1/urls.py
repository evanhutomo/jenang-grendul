from django.contrib import admin
from django.urls import path, re_path, include
from app1 import views

urlpatterns = [
    re_path(r'^app1/', include('app1.urls')),
    re_path(r'^admin/', admin.site.urls),
]
