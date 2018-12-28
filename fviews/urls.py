from django.conf.urls import url
from django.contrib import admin
from fviews import views

urlpatterns = [
    url(r'^fview_temp/', views.fview_test),
    url(r'^registration/', views.registration),
    url(r'^show/', views.showregistration),
]
