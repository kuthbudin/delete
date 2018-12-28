from django.conf.urls import url
from django.contrib import admin
from session1 import views

urlpatterns = [
    url(r'^visits/', views.cookiex),
    url(r'^signup/', views.signup),
]
