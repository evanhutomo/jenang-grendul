from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = i18n_patterns(
    re_path('', include('app.urls')),
)
