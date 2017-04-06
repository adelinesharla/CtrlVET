# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import url

"""Classes de views genericas utilizadas"""
from django.views.generic import View, TemplateView, DetailView, UpdateView, DeleteView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import ProcessFormView
from _functools import reduce

from django.core.urlresolvers import reverse_lazy, reverse


'HttpResponse para uma pagina template indicando que a operação foi realizada (verificar se tal página existe)'
from django.http import HttpResponseRedirect

'Importando Formularios necessários para views'
from .forms import *
'Importando Models necessárias para views'
from .models import *

from django.forms.models import model_to_dict #iterar em object no template

'Importando atributos da model a serem utilizados nas buscas'
import operator
from django.db.models import Q

from django.http import *
from django.template import RequestContext

import socket

from django_tables2 import MultiTableMixin, SingleTableView, RequestConfig
from .tables import *

"""Formulário de cadastro de FichaAtendimentoPequenos"""
class FichaAtendimentoPequenosFormView(FormView):
	#template_name = ''
	form_class = FichaAtendimentoPequenos
	#success_url = ''

	
	def get_context_data(self, **kwargs):
		context = super (FichaAtendimentoPequenosFormView, self).get_context_data(**kwargs)
		context['action_form'] = 'cadastro'
		return context

	def form_valid(self, form):
		novo_form = form.save()		
		return HttpResponseRedirect(reverse_lazy('',args=(novo_form.pk,))) 

	def post(self, form, **kwargs):
		if "cancel" in self.request.POST:
			return HttpResponseRedirect(self.success_url)
		return super(FichaAtendimentoPequenos, self).post(self, form, **kwargs)
		
"""Classe para visualizar FichaAtendimentoPequenos"""
class FichaAtendimentoPequenosDetalhesViewForm(UpdateView):
	form_class = FichaAtendimentoPequenosFormDisable
	model = FichaAtendimentoPequenos
	template_name_suffix = '_detail'
	#success_url = ''

	def get_context_data(self, **kwargs):
		context = super (FichaAtendimentoPequenosDetalhesViewForm, self).get_context_data(**kwargs)
		context['FichaAtendimentoPequenos'] = FichaAtendimentoPequenos.objects.get(pk=self.kwargs.get('pk'))
		context['action_form'] = 'null'
		return context

	def post(self, form, **kwargs):
		if "POST" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		if "GET" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		return super(FichaAtendimentoPequenosDetalhesViewForm, self).post(self, form, **kwargs)

