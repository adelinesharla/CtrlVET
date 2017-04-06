# _*_ coding: utf-8 _*_
"""CtrlVET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
#Importação da classe TemplateView 
from django.views.generic import TemplateView 
from django.contrib import admin
#from templates import *

"""
Classe generic view que renderiza templates para a prototipagem de interface.
"""
class MockUp(TemplateView):
    """
    Essa função recebe como argumento as variáveis de contexto necessárias para 
    renderizar o template através da url definida em url patterns.
    (override da função da generic view Template View).
    """
    def get_context_data(self, **kwargs):
        self.template_name = self.kwargs["template_name"]
        return super(MockUp,self).get_context_data(**kwargs)

    """
    Para que as urls de templates sejam mapeados como view e com os argumentos 
    passados para a função get_context_data.
    """

# Overrides the default 400 handler django.views.defaults.bad_request
handler400 = 'cadastro.bad_request'
# Overrides the default 403 handler django.views.defaults.permission_denied
handler403 = 'cadastro.views.permission_denied'
# Overrides the default 404 handler django.views.defaults.page_not_found
handler404 = 'cadastro.views.page_not_found'
# Overrides the default 500 handler django.views.defaults.server_error
handler500 = 'cadastro.views.server_error'	
	
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^(?P<template_name>.*)$', MockUp.as_view()),
    url(r'', include('cadastro.urls')),
    url(r'', include('financeiro.urls')),
    url(r'', include('consulta.urls')),
    url(r'', include('login.urls')),
    #url(r'^agenda', agenda.html),
]
