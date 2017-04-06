from django.conf.urls import url
from login.views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^main/signup/$', signup, name='signup'),
    url(r'^main/login/$', auth_views.login,{'template_name': 'login/login.html'}, name='login'),
    url(r'^main/logout/$', auth_views.logout, {'template_name': 'login/logout.html'},name='logout'),
]
