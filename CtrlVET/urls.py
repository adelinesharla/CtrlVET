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
from django.conf.urls import url
#Importação da classe TemplateView 
from django.views.generic import TemplateView 
from django.contrib import admin

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
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<template_name>.*)$', MockUp.as_view()),
    
]
