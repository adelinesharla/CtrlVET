# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import url

"""Classes de views genericas utilizadas"""
from django.views.generic import View, TemplateView, DetailView, UpdateView, DeleteView,ListView, FormView

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

#Não somos selvagens. O uso de 2 espaços como forma de identação é degradante.
#Tabs são apropriados e garantem uma maior readability ao código
# :)

"""Classe de renderização da main (sem contexto)"""
class MainView(TemplateView):
	template_name='cadastro/main.html'

#Views relacionadas à classe Tutor:

"""Classe para listar os tutores"""
class ListTutor(ListView):
	model = TutorEndTel
	paginate_by = 10 			

"""Classe de renderização do painel de tutor (sem contexto)"""
class TutorResumo(ListTutor):
	template_name='cadastro/tutor_resumo.html'

'TUTOR FORM VIEW , PARA FORMULARIO DE CADASTRO DO TUTOR'
class TutorFormView(View):
	form_class_tutor = TutorModelForm
	template_formulario = 'cadastro/tutor_form.html'

	def get(self, request):
		form = self.form_class_tutor()
		return render(request, self.template_formulario, {'form':form})
	'Precisei modificar a variável form_class para form_class_tutor e adicionar o form.sve() pra fazer o formulario funcionar'
	'Se estiver errado por favor corrijam'
	def post(self, request):
		form = self.form_class_tutor(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/success/')
		return render(request, self.template_formulario, {'form':form})

"""Classe para deletar Tutor"""
class TutorDeletar(DeleteView):
	model = TutorEndTel
	#success_url = reverse_lazy('tutor_resumo')

"""Classe para retornar detalhes de Tutor (alimenta o template tutor_detalhes)"""
class TutorDetalhesView(DetailView):
	pk_url_kwarg = "tutor_id"
	model = TutorEndTel

	def get_context_data(self, **kwargs):
		context = super (TutorDetalhesView, self).get_context_data(**kwargs)
		return context


"""Classe para editar Tutor"""
class TutorEditar(UpdateView):
	model = TutorEndTel
	template_name_suffix = 'form_update'

"""Classe para busca de Tutor pelos campos: nome, email e cpf"""
class TutorBuscaListView(ListTutor):
    def get_queryset(self):
        result = super(TutorBuscaListView, self).get_queryset()

        query = self.request.GET.get('q')
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

        return result

#Views relacionadas à classe Animal:

"""Classe para listar os animais"""    
class ListAnimal(ListView):
	model = Animal    	
	paginate_by = 10 

"""Classe de renderização do painel de animal (sem contexto)"""
class AnimalResumo(ListAnimal):
	template_name='cadastro/animal_resumo.html'

'ANIMAL FORM VIEW, PARA FORMULARIO DE CADASTRO DO ANIMAL'    
class AnimalFormView(View):
	form_class_animal = AnimalModelForm
	template_formulario = 'cadastro/animal_form.html'

	def get(self, request):
		form = self.form_class_animal()
		return render(request, self.template_formulario, {'form':form})

	def post(self, request):
		form = self.form_class_animal(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/success/')
	
		return render(request, self.template_formulario, {'form':form})

"""Classe para retornar detalhes de Animal (alimenta o template animal_detalhes)"""
class AnimalDetalhesView(DetailView):
	pk_url_kwarg = "animal_id"
	model = Animal
	
	def get_context_data(self, **kwargs):
		context = super (AnimalDetalhesView, self).get_context_data(**kwargs)
		return context

"""Classe para editar Animal"""
class TutorEditar(UpdateView):
	model = Animal
	template_name_suffix = 'form_update'

"""Classe para deletar Animal"""
class TutorDeletar(DeleteView):
	model = Animal
	#success_url = reverse_lazy('animal_resumo') 

"""Classe para busca de Animal pelos campos: nome, rg, especie e raça"""
class AnimalBuscaListView(ListAnimal):
    def get_queryset(self):
        result = super(AnimalBuscaListView, self).get_queryset()

        query = self.request.GET.get('q')
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

        return result

#Views relacionadas à classe Consulta:

class ConsultaFormView(FormView):
	template_name = ''
	form_class = ConsultaModelForm
	success_url = ''
	
	def form_valid(self, form):
		return super(ConsultaFormView,self).form_valid(form)

class ConsultaDeleteView(DeleteView):
	model = Consulta
	#success_url = reverse_lazy('consulta_resumo')

class ConsultaDetailView(DetailView):
	pk_url_kwarg = "consulta_id"
	model = Consulta

	def get_context_data(self, **kwargs):
		context = super (ConsultaDetailView, self).get_context_data(**kwargs)
		return context

class ConsultaUpdateView(UpdateView):
	model = Consulta
	template_name_suffix = 'form_update'

class ConsultaListView(ListView):
	model = Consulta    	
	paginate_by = 10 

class ConsultaResumo(ConsultaListView):
	template_name=''

class ConsultaBuscaListView(ConsultaListView):
	def get_queryset(self):
        	result = super(ConsultaBuscaListView, self).get_queryset()

	        query = self.request.GET.get('q')
	        if query:
	            query_list = query.split()
	            result = result.filter(
	                #reduce(operator.and_,
	                       #(Q(campo1__icontains=q) for q in query_list)) |
			#reduce(operator.and_,
	                       #(Q(campo2__icontains=q) for q in query_list))
	            )
	
	        return result

#Views relacionadas à classe Exame:

class ExameFormView(FormView):
	template_name = ''
	form_class = ExameModelForm
	success_url = ''
	
	def form_valid(self, form):
		return super(ExameFormView,self).form_valid(form)

class ExameDeleteView(DeleteView):
	model = Exame
	#success_url = reverse_lazy('consulta_resumo')

class ExameDetailView(DetailView):
	pk_url_kwarg = "exame_id"
	model = Exame

	def get_context_data(self, **kwargs):
		context = super (ExameDetailView, self).get_context_data(**kwargs)
		return context

class ExameUpdateView(UpdateView):
	model = Exame
	template_name_suffix = 'form_update'

class ExameListView(ListView):
	model = Exame    	
	paginate_by = 10 

class ExameResumo(ExameListView):
	template_name=''

class ExameBuscaListView(ExameListView):
	def get_queryset(self):
	       	result = super(ExameBuscaListView, self).get_queryset()
	        query = self.request.GET.get('q')
	        if query:
	            query_list = query.split()
	            result = result.filter(
	                #reduce(operator.and_,
	                       #(Q(campo1__icontains=q) for q in query_list)) |
			#reduce(operator.and_,
	                       #(Q(campo2__icontains=q) for q in query_list))
	            )
	
	        return result
