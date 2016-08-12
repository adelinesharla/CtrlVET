# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import url
from django.views.generic import View, TemplateView, DetailView, UpdateView
'HttpResponse para uma pagina template indicando que a operação foi realizada (verificar se tal página existe)'
from django.http import HttpResponseRedirect
'Imortando Formularios necessários para views de tutor e animal'
from .forms import TutorModelForm, AnimalModelForm
from .models import *

#Não somos selvagens. O uso de 2 espaços como forma de identação é degradante.
#Tabs são apropriados e garantem uma maior readability ao código
# :)

"""Classe de renderização da main (sem contexto)"""
class MainView(TemplateView):
	template_name='cadastro/main.html'

'TUTOR FORM VIEW , PARA FORMULARIO DE CADASTRO DO TUTOR'
class TutorFormView(View):
	form_class_tutor = TutorModelForm
	template_formulario = 'cadastro/form.html'

	def get(self, request):
		form = self.form_class_tutor()
		return render(request, self.template_formulario, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/success/')
		return render(request, self.template_formulario, {'form':form})


"""Classe para retornar detalhes de Tutor (alimenta o template tutor_detalhes)"""
class TutorDetalhesView(DetailView):
	model = Tutor

	def get_context_data(self):
		context = super (TutorDetalhesView, self).get_context_data()
		return context

"""Classe para editar Tutor"""
class TutorEditar(UpdateView):
	model = Tutor
	template_name_suffix = '_update_form'

'ANIMAL FORM VIEW, PARA FORMULARIO DE CADASTRO DO ANIMAL'    
class AnimalFormView(View):
	form_class_animal = AnimalModelForm
	template_formulario = 'cadastro/form.html'

	def get(self, request):
		form = self.form_class_animal()
		return render(request, self.template_formulario, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/success/')
	
		return render(request, self.template_formulario, {'form':form})

"""Classe para retornar detalhes de Animal (alimenta o template animal_detalhes)"""
class AnimalDetalhesView(DetailView):

	model = Animal
	
	def get_context_data(self):
		context = super (AnimalDetalhesView, self).get_context_data()
		return context

"""Classe para editar Animal"""
class TutorEditar(UpdateView):
	model = Animal
	template_name_suffix = '_update_form'
