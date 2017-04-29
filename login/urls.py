from django.conf.urls import url, include
from login.views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^main/signup/$', signup, name='signup'),
    url(r'^main/login/$', auth_views.login,{'template_name': 'login/login.html'}, name='login'),
    url(r'^main/logout/$', auth_views.logout, {'template_name': 'login/logout.html'},name='logout'),
    url(r'^main/veterinario/$', TemplateView.as_view(template_name='veterinario_auth.html')),
    url(r'^main/secretario/$', TemplateView.as_view(template_name='secretario_auth.html')),
    url(r'^main/tecnico/$', TemplateView.as_view(template_name='tecnico_auth.html')),
]