from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import login
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^fviews/', include('fviews.urls')),
    url('^session1/', include('session1.urls')),
    url('^login/', auth_views.LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    url('^logout/', auth_views.LogoutView.as_view(), {'template_name': 'registration/logout.html'}, name='logout'),

]
