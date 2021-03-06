# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import url

"""Classes de views genericas utilizadas"""
from django.views.generic import View, TemplateView, DetailView, UpdateView, DeleteView, ListView, FormView, RedirectView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import ProcessFormView
from _functools import reduce

from django.core.urlresolvers import reverse_lazy, reverse


'HttpResponse para uma pagina template indicando que a operação foi realizada (verificar se tal página existe)'
from django.http import HttpResponseRedirect

'Importando Formularios necessários para views de tutor e animal'
from .forms import *
'Importando Models necessárias para views de tutor e animal'
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

		
def page_not_found(request):
	# Dict to pass to template, data could come from DB query
	values_for_template = {}
	return render(request,'404.html',values_for_template,status=404)

def server_error(request):
	# Dict to pass to template, data could come from DB query
	values_for_template = {}
	return render(request,'500.html',values_for_template,status=500)

def bad_request(request):
	# Dict to pass to template, data could come from DB query
	values_for_template = {}
	return render(request,'400.html',values_for_template,status=400)

def permission_denied(request):
	# Dict to pass to template, data could come from DB query
	values_for_template = {}
	return render(request,'403.html',values_for_template,status=403)


	
"""Classe de renderização da main (sem contexto)"""
class MainView(TemplateView):
	template_name='cadastro/main.html'
	def get(self,*args):
		if (self.request.user.groups.filter(name='Veterinário').exists()):
			return HttpResponseRedirect('veterinario')
	        if(self.request.user.is_anonymous):
			return HttpResponseRedirect('login')
		if(self.request.user.groups.filter(name='Técnico').exists()):
			return HttpResponseRedirect('tecnico')
		if(self.request.user.groups.filter(name='Secretário').exists()):
			return HttpResponseRedirect('secretario')
		else:
			return HttpResponseRedirect('vazia')

class MainVaziaView(TemplateView):
	template_name='cadastro/main.html'

class SecretarioView(TemplateView):
	template_name='secretario_auth.html'

class VeterinarioView(TemplateView):
	template_name='veterinario_auth.html'

class TecnicoView(TemplateView):
	template_name='tecnico_auth.html'

class SuccessView(TemplateView):
	template_name='cadastro/success.html'	

#Views relacionadas à classe Tutor:

"""Classe para listar os tutores"""


class ListTutor(SingleTableView):
	model = TutorEndTel
	table_class = TutorEndTelTable
	table_pagination = {
		'per_page': 10
	}

	def get_context_data(self, **kwargs):
		context = super (ListTutor, self).get_context_data(**kwargs)
		context['form'] = TutorBuscaAdvForm()
		context['action_search'] = reverse_lazy('tutor_busca_list_view', urlconf=None, args=None, kwargs=None)
		context['action_add'] = reverse_lazy('tutor_cadastro', urlconf=None, args=None, kwargs=None)
		return context

"""Classe de renderização do painel de tutor (sem contexto)"""
class TutorResumo(ListTutor):
	template_name='cadastro/tutor_resumo.html'

"""Classe de renderização do painel de tutor (sem contexto)"""
class TutorResumoSucesso(ListTutor):
	template_name='cadastro/tutor_resumo_sucesso.html'


"""Formulário de cadastro de Tutor"""
class TutorFormView(FormView):
	template_name = 'cadastro/tutorendtel_form.html'
	form_class = TutorModelForm
	success_url = '/tutor/resumo'

	
	def get_context_data(self, **kwargs):
		context = super (TutorFormView, self).get_context_data(**kwargs)
		context['action_form'] = 'cadastro'
		return context

	def form_valid(self, form):
		novo_form = form.save()		
		return HttpResponseRedirect(reverse_lazy('tutor_success',args=(novo_form.pk,))) 

	def post(self, form, **kwargs):
		if "cancel" in self.request.POST:
			return HttpResponseRedirect(self.success_url)
		return super(TutorFormView, self).post(self, form, **kwargs)

"""Classe para deletar Tutor"""
class TutorDeletar(DeleteView):
	model = TutorEndTel
	success_url = '/tutor/resumo/sucesso'
		

"""Classe para retornar detalhes de Tutor (alimenta o template tutor_detalhes)"""		
class TutorDetalhesViewSuccess(DetailView):
	model = TutorEndTel

	def get_context_data(self, **kwargs):
		context = super (TutorDetalhesViewSuccess, self).get_context_data(**kwargs)
		return context

"""Classe para editar Tutor"""
class TutorDetalhesViewSuccessForm(UpdateView):
	form_class = TutorModelFormDisable
	model = TutorEndTel
	template_name_suffix = '_success'
	success_url = '/tutor/resumo'

	def get_context_data(self, **kwargs):
		context = super (TutorDetalhesViewSuccessForm, self).get_context_data(**kwargs)
		context['tutor'] = TutorEndTel.objects.get(pk=self.kwargs.get('pk'))
		context['action_form'] = 'null'
		return context

	def post(self, form, **kwargs):
		if "POST" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		if "GET" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		return super(TutorDetalhesViewSuccessForm, self).post(self, form, **kwargs)		
		
"""Classe para visualizar Tutor"""
class TutorDetalhesViewForm(UpdateView):
	form_class = TutorModelFormDisable
	model = TutorEndTel
	template_name_suffix = '_detail'
	success_url = '/tutor/resumo'

	def get_context_data(self, **kwargs):
		context = super (TutorDetalhesViewForm, self).get_context_data(**kwargs)
		context['tutor'] = TutorEndTel.objects.get(pk=self.kwargs.get('pk'))
		context['action_form'] = 'null'
		return context

	def post(self, form, **kwargs):
		if "POST" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		if "GET" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		return super(TutorDetalhesViewForm, self).post(self, form, **kwargs)

"""Classe para editar Tutor"""
class TutorEditar(UpdateView):
	form_class = TutorModelForm
	model = TutorEndTel
	template_name_suffix = '_form_update'
	success_url = '/tutor/resumo/sucesso'
	success_url2 = '/tutor/resumo'
	
	def get_context_data(self, **kwargs):
		context = super (TutorEditar, self).get_context_data(**kwargs)
		context['action_form'] = 'update'
		return context

	def post(self, form, **kwargs):
		if "cancel" in self.request.POST:
			self.object = self.get_object()
			return HttpResponseRedirect(self.success_url2)
		return super(TutorEditar, self).post(self, form, **kwargs)



"""Classe para busca de Tutor pelos campos: nome, email e cpf"""
class TutorBuscaListView(SingleTableView):
	model = TutorEndTel
	table_class = TutorEndTelTable
	form_class = TutorBuscaAdvForm
	
	table_pagination = {
		'per_page': 10
	}

	def get_queryset(self):
		result = super(TutorBuscaListView, self).get_queryset()		
		query = self.request.GET.get('q')
		form = self.form_class(self.request.GET or None)

		if query:
			query_list = query.split()
			result = result.filter(
				reduce(operator.and_,
					   (Q(_nome__icontains=q) for q in query_list)) |
				reduce(operator.and_,
					   (Q(_email__icontains=q) for q in query_list)) |
		reduce(operator.and_,
					   (Q(_cpf__icontains=q) for q in query_list))
			)
	
		else:
			if form.is_valid():
				if form.cleaned_data['_nome']:
					result = result.filter(_nome__icontains=form.cleaned_data['_nome'])
				if form.cleaned_data['_cpf']:
					result = result.filter(_cpf__icontains=form.cleaned_data['_cpf'])
				if form.cleaned_data['_email']:
					result = result.filter(_email__icontains=form.cleaned_data['_email'])
				if form.cleaned_data['_bairro']:
					result = result.filter(_bairro__icontains=form.cleaned_data['_bairro'])
				if form.cleaned_data['_cidade']:
					result = result.filter(_cidade__icontains=form.cleaned_data['_cidade'])
				if form.cleaned_data['_cep']:
					result = result.filter(_cep__icontains=form.cleaned_data['_cep'])
				if form.cleaned_data['_uf']:
					result = result.filter(_uf__icontains=form.cleaned_data['_uf'])	

		return result

	def get_context_data(self, **kwargs):
		context = super (TutorBuscaListView, self).get_context_data(**kwargs)
		context['form'] = TutorBuscaAdvForm()
		context['action_search'] = reverse_lazy('tutor_busca_list_view', urlconf=None, args=None, kwargs=None)
		context['action_add'] = reverse_lazy('tutor_cadastro', urlconf=None, args=None, kwargs=None)
		return context


#Views relacionadas à classe Animal:

"""Classe para listar os animais"""    
class ListAnimal(SingleTableView):
	model = Animal
	table_class = AnimalTable
	table_pagination = {
		'per_page': 10
	}

	def get_context_data(self, **kwargs):
		context = super (ListAnimal, self).get_context_data(**kwargs)
		context['form'] = AnimalBuscaAdvForm()
		context['action_search'] = reverse_lazy('animal_busca_list_view', urlconf=None, args=None, kwargs=None)
		context['action_add'] = reverse_lazy('animal_cadastro', urlconf=None, args=None, kwargs=None)
		return context


"""Classe de renderização do painel de animal (sem contexto)"""
class AnimalResumo(ListAnimal):
	template_name='cadastro/animal_resumo.html'
	
	def get_context_data(self, **kwargs):
		context = super (AnimalResumo, self).get_context_data(**kwargs)
		context['form'] = AnimalBuscaAdvForm()
		return context
		
"""Classe de renderização do painel de animal (sem contexto)"""
class AnimalResumoSucesso(ListAnimal):
	template_name='cadastro/animal_resumo_sucesso.html'
	
	def get_context_data(self, **kwargs):
		context = super (AnimalResumoSucesso, self).get_context_data(**kwargs)
		context['form'] = AnimalBuscaAdvForm()
		return context


"""Formulário de cadastro de Animal"""
class AnimalFormView(FormView):
	template_name = 'cadastro/animal_form.html'
	form_class = AnimalModelForm
	success_url = '/animal/resumo'

	def get_context_data(self, **kwargs):
		context = super (AnimalFormView, self).get_context_data(**kwargs)
		context['action_form'] = 'cadastro'
		return context
	
	def form_valid(self, form):
		novo_form = form.save()		
		return HttpResponseRedirect(reverse_lazy('animal_detalhes_sucesso',args=(novo_form.pk,))) 

	def post(self, form, **kwargs):
		if "cancel" in self.request.POST:
			return HttpResponseRedirect(self.success_url)
		return super(AnimalFormView, self).post(self, form, **kwargs)
	
"""Classe para retornar detalhes de Animal (alimenta o template animal_detalhes)"""
class AnimalDetalhesViewSuccess(DetailView):
	model = Animal

	def get_context_data(self, **kwargs):
		context = super (AnimalDetalhesViewSuccess, self).get_context_data(**kwargs)
		return context

class AnimalDetalhesViewSuccessForm(UpdateView):
	form_class = AnimalModelFormDisable
	model = Animal
	template_name_suffix = '_success'
	success_url = '/animal/resumo'

	def get_context_data(self, **kwargs):
		context = super (AnimalDetalhesViewSuccessForm, self).get_context_data(**kwargs)
		context['animal'] = Animal.objects.get(pk=self.kwargs.get('pk'))
		context['action_form'] = 'null'
		return context

	def post(self, form, **kwargs):
		if "POST" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		if "GET" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		return super(AnimalDetalhesViewSuccessForm, self).post(self, form, **kwargs)

"""Classe para retornar detalhes de Animal (alimenta o template animal_detalhes)"""

class AnimalDetalhesViewForm(UpdateView):
	form_class = AnimalModelFormDisable
	model = Animal
	template_name_suffix = '_detail'
	success_url = '/animal/resumo'

	def get_context_data(self, **kwargs):
		context = super (AnimalDetalhesViewForm, self).get_context_data(**kwargs)
		context['animal'] = Animal.objects.get(pk=self.kwargs.get('pk'))
		context['action_form'] = 'null'
		return context

	def post(self, form, **kwargs):
		if "POST" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		if "GET" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		return super(AnimalDetalhesViewForm, self).post(self, form, **kwargs)


"""Classe para editar Animal"""
class AnimalEditar(UpdateView):
	form_class = AnimalModelForm
	#fields = '__all__'
	model = Animal
	template_name_suffix = '_form_update'
	success_url = '/animal/resumo/sucesso'
	success_url2 = '/animal/resumo'

	def get_context_data(self, **kwargs):
		context = super (AnimalEditar, self).get_context_data(**kwargs)
		context['action_form'] = 'update'
		return context

	def post(self, form, **kwargs):
		if "cancel" in self.request.POST:
			self.object = self.get_object()
			return HttpResponseRedirect(self.success_url2)
		return super(AnimalEditar, self).post(self, form, **kwargs)

class AnimalObito(UpdateView):
	form_class = AnimalObitoForm
	model = Animal
	template_name_suffix = '_form_update_obito'
	success_url = '/animal/resumo/sucesso'
	success_url2 = '/animal/resumo'
	
	def get_context_data(self, **kwargs):
		context = super (AnimalObito, self).get_context_data(**kwargs)
		context['action_form'] = 'update'
		return context
		
	def post(self, form, **kwargs):
		if "cancel" in self.request.POST:
			self.object = self.get_object()
			return HttpResponseRedirect(self.success_url2)
		return super(AnimalObito, self).post(self, form, **kwargs)

"""Classe para deletar Animal"""
class AnimalDeletar(DeleteView):
	model = Animal
	success_url = '/animal/resumo/sucesso'

"""Classe para busca de Animal pelos campos: nome, rg, especie e raça"""
class AnimalBuscaListView(SingleTableView):
	model = Animal
	table_class = AnimalTable
	form_class = AnimalBuscaAdvForm
	
	table_pagination = {
		'per_page': 10
	}

	def get_queryset(self):
		result = super(AnimalBuscaListView, self).get_queryset()		
		query = self.request.GET.get('q')
		form = self.form_class(self.request.GET or None)

		if query:
			query_list = query.split()
			result = result.filter(
				reduce(operator.and_,
					   (Q(_nome__icontains=q) for q in query_list)) |
				reduce(operator.and_,
					   (Q(_rg__icontains=q) for q in query_list)) |
		reduce(operator.and_,
					   (Q(_especie__icontains=q) for q in query_list)) |
		reduce(operator.and_,
					   (Q(_raca__icontains=q) for q in query_list))
			)

		else:
			if form.is_valid():

				if form.cleaned_data['_animal']:
					result = result.filter(_nome__icontains=form.cleaned_data['_animal'])
				if form.cleaned_data['_rg']:
					result = result.filter(_rg__icontains=form.cleaned_data['_rg'])
				if form.cleaned_data['_raca']:
					result = result.filter(_raca__icontains=form.cleaned_data['_raca'])
				if form.cleaned_data['sexo']:
					result = result.filter(sexo__icontains=form.cleaned_data['sexo'])
				if form.cleaned_data['_idade']:
					result = result.filter(_idade__icontains=form.cleaned_data['_idade'])
				if form.cleaned_data['_especie']:
					result = result.filter(_especie__icontains=form.cleaned_data['_especie'])
				
				'''if form.cleaned_data['_tutor']:
																	result = result.filter(tutor=TutorEndTel.objects.filter(_nome__icontains=form.cleaned_data['_tutor']))'''

					#result = Animal.objects.filter(_tutor__icontains=tutor for tutor in tutores)

		return result

	def get_context_data(self, **kwargs):
		context = super (AnimalBuscaListView, self).get_context_data(**kwargs)
		context['form'] = AnimalBuscaAdvForm()
		context['action_search'] = reverse_lazy('animal_busca_list_view', urlconf=None, args=None, kwargs=None)
		context['action_add'] = reverse_lazy('animal_cadastro', urlconf=None, args=None, kwargs=None)
		return context	
			

#Views relacionadas à classe Consulta:

class ConsultaFormView(FormView):
	template_name = 'cadastro/consulta_form.html'
	form_class = ConsultaModelForm
	success_url = '/consulta/resumo'

	def get_context_data(self, **kwargs):
		context = super (ConsultaFormView, self).get_context_data(**kwargs)
		context['action_form'] = 'cadastro'
		return context
	

	def form_valid(self, form):
		#form.laboratorio = Laboratorio.objects.get(pk=self.kwargs.get('pk'))
		animal = form.cleaned_data['animal']
		consulta = form.save()
		consulta.cliente = Animal.objects.get(pk=animal.pk).tutor
		consulta.save()
		return HttpResponseRedirect(reverse_lazy('consulta_detalhes_sucesso',args=(consulta.pk,))) 

	def get_initial(self):
		initial=super(ConsultaFormView, self).get_initial()
		initial['retorno'] = False
		return initial

class ConsultaDeleteView(DeleteView):
	model = Consulta
	success_url = '/consulta/resumo/sucesso'
	#success_url = reverse_lazy('consulta_resumo')

class ConsultaDetailView(DetailView):
	model = Consulta

	def get_context_data(self, **kwargs):
		context = super (ConsultaDetailView, self).get_context_data(**kwargs)
		return context

class ConsultaDetailViewForm(UpdateView):
	form_class = ConsultaModelFormDisable
	model = Consulta
	template_name_suffix = '_detail'
	success_url = '/consulta/resumo'

	def get_context_data(self, **kwargs):
		context = super (ConsultaDetailViewForm, self).get_context_data(**kwargs)
		context['animal'] = Consulta.objects.get(pk=self.kwargs.get('pk')).animal
		context['action_form'] = 'null'
		return context

	def post(self, form, **kwargs):
		if "POST" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		if "GET" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		return super(ConsultaDetailViewForm, self).post(self, form, **kwargs)

class ConsultaDetailViewSuccess(DetailView):
	model = Consulta

	def get_context_data(self, **kwargs):
		context = super (ConsultaDetailViewSuccess, self).get_context_data(**kwargs)
		return context

class ConsultaDetailViewSuccessForm(UpdateView):
	form_class = ConsultaModelFormDisable
	model = Consulta
	template_name_suffix = '_success'
	success_url = '/consulta/resumo'

	def get_context_data(self, **kwargs):
		context = super (ConsultaDetailViewSuccessForm, self).get_context_data(**kwargs)
		context['animal'] = Consulta.objects.get(pk=self.kwargs.get('pk')).animal
		context['action_form'] = 'null'
		return context

	def post(self, form, **kwargs):
		if "POST" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		if "GET" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		return super(ConsultaDetailViewSuccessForm, self).post(self, form, **kwargs)

class ConsultaUpdateView(UpdateView):
	form_class = ConsultaModelForm
	model = Consulta
	template_name_suffix = '_form_update'
	success_url = '/success/'

	def get_context_data(self, **kwargs):
		context = super (ConsultaUpdateView, self).get_context_data(**kwargs)
		context['action_form'] = 'update'
		return context

class ConsultaListView(SingleTableView):
	model = Consulta
	table_class = ConsultaTable 	
	table_pagination = {
		'per_page': 10
	}

	def get_context_data(self, **kwargs):
		context = super (ConsultaListView, self).get_context_data(**kwargs)
		context['form'] = ConsultaBuscaAdvForm()
		context['action_search'] = reverse_lazy('consulta_busca_list_view', urlconf=None, args=None, kwargs=None)
		context['action_add'] = reverse_lazy('consulta_cadastro', urlconf=None, args=None, kwargs=None)
		return context


class ConsultaResumo(ConsultaListView):
	template_name='cadastro/consulta_resumo.html'

class ConsultaResumoSucesso(ConsultaListView):
	template_name='cadastro/consulta_resumo_success.html'

class ConsultaBuscaListView(ConsultaListView):
	def get_queryset(self):
			result = super(ConsultaBuscaListView, self).get_queryset()

			query = self.request.GET.get('q')
			if query:
				query_list = query.split()
				result = result.filter(
					reduce(operator.and_,
						   (Q(_data__icontains=q) for q in query_list)) |
			reduce(operator.and_,
						   (Q(_diagnostico__icontains=q) for q in query_list))|
			reduce(operator.and_,
						   (Q(_retorno__icontains=q) for q in query_list))|
			reduce(operator.and_,
						   (Q(animal___nome__icontains=q) for q in query_list))|
			reduce(operator.and_,
						   (Q(veterinario___nome__icontains=q) for q in query_list))
				)
	
			return result
			
"""Classe para fazer a busca avancada dos atributos de consulta"""	       	        
class ConsultaBuscaAvancadaMixin(ListView,FormView):
	form = ConsultaBuscaAdvForm
	form_class = ConsultaBuscaAdvForm
	template_name = 'cadastro/consulta_resumo.html'
	success_url = '/success/'
	
	query=Consulta.objects.all()
	
	def get(request,*args):
		if request.method == 'POST':
			form = ConsultaBuscaAdvForm(request.POST)
			i = 0
			while i < len(query):
				if ((form.animal == None) | (query[i].animal.nome__icontains__form.animal)):
					if ((form.veterinario == None) | (query[i].veterinario.nome__icontains__form.veterinario)): 
						if ((form.data == None) | (query[i].data__icontains__form.data)):
							lista_retornavel += query[i]
				i = i+1		
					
				
		else:
			ConsultaBuscaAdvForm()

		#return lista_retornavel
		return HttpResponseRedirect('/consulta/resumo')	        

#Views relacionadas à classe Exame:

class ExameFormView(FormView):
	template_name = 'cadastro/exame_form.html'
	form_class = ExameModelForm
	success_url = '/exames'

	def get_context_data(self, **kwargs):
		context = super (ExameFormView, self).get_context_data(**kwargs)
		context['action_form'] = 'cadastro'
		return context
	
	def form_valid(self, form, **kwargs):
		form.laboratorio = Laboratorio.objects.get(pk=self.kwargs.get('pk'))
		novo_form=form.save()
                return HttpResponseRedirect(reverse_lazy('exame_detalhes_sucesso',args=(novo_form.pk,)))

	def get_initial(self):
		super(ExameFormView, self).get_initial()
		laboratorio = Laboratorio.objects.get(pk=self.kwargs.get('pk'))
		self.initial = {"laboratorio":laboratorio}
		return self.initial

class ExameDeleteView(DeleteView):
	model = Exame
	success_url = '/exame/resumo'
	#success_url = reverse_lazy('consulta_resumo')

class ExameDetailView(DetailView):
	model = Exame

	def get_context_data(self, **kwargs):
		context = super (ExameDetailView, self).get_context_data(**kwargs)
		return context

class ExameDetailViewForm(UpdateView):
	form_class = ExameModelFormDisable
	model = Exame
	template_name_suffix = '_detail'
	success_url = 'exames'

	def get_context_data(self, **kwargs):
		context = super (ExameDetailViewForm, self).get_context_data(**kwargs)
		context['action_form'] = 'null'
		return context

	def post(self, form, **kwargs):
		if "POST" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		if "GET" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		return super(ExameDetailViewForm, self).post(self, form, **kwargs)

class ExameDetailViewSuccess(DetailView):
	model = Exame

	def get_context_data(self, **kwargs):
		context = super (ExameDetailViewSuccessView, self).get_context_data(**kwargs)
		return context

class ExameDetailViewSucessForm(UpdateView):
	form_class = ExameModelFormDisable
	model = Exame
	template_name_suffix = '_success'
	success_url = '/exame/resumo'

	def get_context_data(self, **kwargs):
		context = super (ExameDetailViewSucessForm, self).get_context_data(**kwargs)
		context['action_form'] = 'null'
		return context

	def post(self, form, **kwargs):
		if "POST" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		if "GET" in self.request.POST:
			return HttpResponseRedirect(self.permission_denied)
		return super(ExameDetailViewSucessForm, self).post(self, form, **kwargs)

class ExameUpdateView(UpdateView):
	model = Exame
	template_name_suffix = '_form_update'
	form_class = ExameModelForm
	success_url = '/success/'

	def get_context_data(self, **kwargs):
		context = super (ExameUpdateView, self).get_context_data(**kwargs)
		context['action_form'] = 'update'
		return context

class ExameListView(ListView):
	model = Exame    	
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super (ExameListView, self).get_context_data(**kwargs)
		context['form'] = ExameBuscaAdvForm()
		context['action_search'] = reverse_lazy('exame_busca_list_view', urlconf=None, args=None, kwargs=None)
		context['action_add'] = reverse_lazy('exame_cadastro', urlconf=None, args=None, kwargs=None)
		return context


class ExameBuscaListView(ExameListView):
	def get_queryset(self):
			result = super(ExameBuscaListView, self).get_queryset()
			query = self.request.GET.get('q')
			if query:
				query_list = query.split()
				result = result.filter(
					reduce(operator.and_,
						   (Q(_data__icontains=q) for q in query_list)) |
			reduce(operator.and_,
						   (Q(_diagnostico__icontains=q) for q in query_list)) |
			reduce(operator.and_,
						   (Q(animal___nome__icontains=q) for q in query_list))|
			reduce(operator.and_,
						   (Q(tecnico___nome__icontains=q) for q in query_list)) |
			reduce(operator.and_,
						   (Q(veterinario___nome__icontains=q) for q in query_list))
				)
	
			return result      

class ExameConcliur(View):
	model = Exame
	success_url = 'exames/laboratorio/detalhes/'

	def get(self, args, **kwargs):
		exame =  Exame.objects.get(pk=self.kwargs['pk'])
		exame._resultado = "Concluido"
		pk=exame.laboratorio.pk
		exame.save()
		return HttpResponseRedirect('/exames/laboratorio/detalhes/'+str(pk))

#Views relacionadas à classe Laboratorio:

class LaboratorioListView(ListView):
	model = Laboratorio    	
	paginate_by = 10 

class LaboratorioResumo(LaboratorioListView):
	template_name='cadastro/laboratorio_resumo.html'

class LaboratorioResumoSucesso(LaboratorioListView):
	template_name='cadastro/laboratorio_resumo_sucesso.html'
	

class LaboratorioDetailView(SingleTableView):
	pk_url_kwarg = "laboratorio_id"
	model = Exame
	table_class = ExameTable
	template_name = 'cadastro/laboratorio_detail.html'
	table_pagination = {
		'per_page': 5
	}
	
	def get_context_data(self, **kwargs):
		context = super (LaboratorioDetailView, self).get_context_data(**kwargs)
		context['form'] = ExameBuscaAdvForm()
		context['action_search'] = reverse_lazy('exame_busca_list_view')
		context['object'] = Laboratorio.objects.get(pk=self.kwargs.get('laboratorio_id'))
		pk = self.kwargs.get('laboratorio_id')
		context['action_add'] = reverse('exame_cadastro', kwargs={'pk': pk})
		context['table_concluidos'] = ExameConcluido(Exame.objects.all().filter(_resultado='Concluido'), prefix="1-")
		return context

	def get_table_data(self, **kwargs):
		if self.table_data is not None:
			return self.table_data
		elif hasattr(self, 'object_list'):
			return self.object_list.filter(laboratorio=self.kwargs.get('laboratorio_id')).filter(_resultado='Pendente')
