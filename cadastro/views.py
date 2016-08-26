# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import url

"""Classes de views genericas utilizadas"""
from django.views.generic import View, FormView, TemplateView, DetailView, UpdateView, DeleteView, ListView, FormView

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



from django.core.urlresolvers import reverse_lazy



#Não somos selvagens. O uso de 2 espaços como forma de identação é degradante.
#Tabs são apropriados e garantem uma maior readability ao código
# :)

"""Classe de renderização da main (sem contexto)"""
class MainView(TemplateView):
	template_name='cadastro/main.html'

class SuccessView(TemplateView):
	template_name='cadastro/success.html'	

#Views relacionadas à classe Tutor:

"""Classe para listar os tutores"""
class ListTutor(ListView):
	model = TutorEndTel
	paginate_by = 10	

"""Classe de renderização do painel de tutor (sem contexto)"""
class TutorResumo(ListTutor):
	template_name='cadastro/tutor_resumo.html'

"""Formulário de cadastro de Tutor"""
class TutorFormView(FormView):
	template_name = 'cadastro/tutorendtel_form.html'
	form_class = TutorModelForm
	success_url = '/success/'

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/success/')


"""Classe para deletar Tutor"""
class TutorDeletar(DeleteView):
	model = TutorEndTel
	#success_url = reverse_lazy('tutor_resumo')
	success_url = '/success/'

"""Classe para retornar detalhes de Tutor (alimenta o template tutor_detalhes)"""
class TutorDetalhesView(DetailView):
	pk_url_kwarg = "tutor_id"
	model = TutorEndTel

	def get_context_data(self, **kwargs):
		context = super (TutorDetalhesView, self).get_context_data(**kwargs)
		return context


"""Classe para editar Tutor"""
class TutorEditar(UpdateView):
	form_class = TutorModelForm
	model = TutorEndTel
	#fields = '__all__'
	template_name_suffix = '_form_update'
	success_url = '/success/'
	#ainda não faço ideia de como fazer isso funcionar



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

"""Formulário de cadastro de Animal"""
class AnimalFormView(FormView):
	template_name = 'cadastro/animal_form.html'
	form_class = AnimalModelForm
	success_url = '/success/'

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/success/')

"""Classe para retornar detalhes de Animal (alimenta o template animal_detalhes)"""
class AnimalDetalhesView(DetailView):
	pk_url_kwarg = "animal_id"
	model = Animal
	
	def get_context_data(self, **kwargs):
		context = super (AnimalDetalhesView, self).get_context_data(**kwargs)
		return context

"""Classe para editar Animal"""
class AnimalEditar(UpdateView):
	form_class = AnimalModelForm
	#fields = '__all__'
	model = Animal
	template_name_suffix = '_form_update'

"""Classe para deletar Animal"""
class AnimalDeletar(DeleteView):
	model = Animal
	success_url = '/success/'

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
	template_name = 'cadastro/consulta_form.html'
	form_class = ConsultaModelForm
	success_url = '/success/'
	
	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/success/')

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
	template_name='cadastro/consulta_resumo.html'

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
	                       (Q(animal__icontains=q) for q in query_list))|
			reduce(operator.and_,
	                       (Q(veterinario__icontains=q) for q in query_list))
	            )
	
	        return result

#Views relacionadas à classe Exame:

class ExameFormView(FormView):
	template_name = ''
	form_class = ExameModelForm
	success_url = ''
	
	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/success/')

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

#Views relacionadas à classe Laboratorio:

class LaboratorioFormView(FormView):
	template_name = ''
	form_class = LaboratorioModelForm
	success_url = ''
	
	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/success/')

class LaboratorioDeleteView(DeleteView):
	model = Laboratorio
	#success_url = reverse_lazy('laboratorio_resumo')

class LaboratorioDetailView(DetailView):
	pk_url_kwarg = "laboratorio_id"
	model = Laboratorio

	def get_context_data(self, **kwargs):
		context = super (LaboratorioDetailView, self).get_context_data(**kwargs)
		return context

class LaboratorioUpdateView(UpdateView):
	model = Laboratorio
	template_name_suffix = 'form_update'

class LaboratorioListView(ListView):
	model = Laboratorio    	
	paginate_by = 10 

"""class LaboratorioResumo(LaboratorioListView):
	template_name=''
	pk_last=(Laboratorio.objects.last()).pk
	list_last_labs=Laboratorio.objects.filter(pk__lte=pk_last)"""
