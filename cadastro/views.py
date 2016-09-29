# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import url

"""Classes de views genericas utilizadas"""
from django.views.generic import View, FormView, TemplateView, DetailView, UpdateView, DeleteView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import ProcessFormView

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

	def get_context_data(self, **kwargs):
		context = super (TutorResumo, self).get_context_data(**kwargs)
		context['form'] = TutorBuscaAdvForm()
		return context


"""Formulário de cadastro de Tutor"""
class TutorFormView(FormView):
	template_name = 'cadastro/tutorendtel_form.html'
	form_class = TutorModelForm
	success_url = '/tutor/resumo'
	

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect(self.success_url)

	def post(self, form, **kwargs):
		if "cancel" in self.request.POST:
        		return HttpResponseRedirect(self.success_url)
		return super(TutorFormView, self).post(self, form, **kwargs)

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
	success_url = '/tutor/resumo'

	def post(self, form, **kwargs):
		if "cancel" in self.request.POST:
			self.object = self.get_object()
        		return HttpResponseRedirect(self.success_url)
		return super(TutorEditar, self).post(self, form, **kwargs)



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
        
"""Classe para fazer a busca avancada dos atributos de tutor"""        
class TutorBuscaAvancadaMixin(FormView):
	form = TutorBuscaAdvForm
	form_class = TutorBuscaAdvForm
	template_name = 'cadastro/tutor_resumo.html'
	success_url = '/success/'
	
	query=TutorEndTel.objects.all()
	

	
	def get(request,*args):
		if request.method == 'POST':
			form = TutorBuscaAdvForm(request.POST)
			i = 0
			while i < len(query):
				if ((form.nome == None) | (query[i].nome__icontains__form.nome)):
					if ((form.cpf == None) | (query[i].cpf__icontains__form.cpf)): 
						if ((form.email == None) | (query[i].email__icontains__form.email)): 	
							if ((form.bairro == None) | (query[i].endereco.bairro__icontains__form.bairro)): 
								if ((form.cidade == None) | (query[i].endereco.cidade__icontains__form.cidade)):
									if ((form.cep == None) | (query[i].endereco.cep__icontains__form.cep)): 
										if ((form.uf == None) | (query[i].endereco.uf__icontains__form.uf)):  
											lista_retornavel += query[i]
				i = i+1		
					
				
		else:
			TutorBuscaAdvForm()

#Views relacionadas à classe Animal:

"""Classe para listar os animais"""    
class ListAnimal(ListView):
	model = Animal    	
	paginate_by = 10 

"""Classe de renderização do painel de animal (sem contexto)"""
class AnimalResumo(ListAnimal):
	template_name='cadastro/animal_resumo.html'
	
	def get_context_data(self, **kwargs):
		context = super (AnimalResumo, self).get_context_data(**kwargs)
		context['form'] = AnimalBuscaAdvForm()
		return context


"""Formulário de cadastro de Animal"""
class AnimalFormView(FormView):
	template_name = 'cadastro/animal_form.html'
	form_class = AnimalModelForm
	success_url = '/animal/resumo'

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/animal/resumo')

	def post(self, form, **kwargs):
		if "cancel" in self.request.POST:
        		return HttpResponseRedirect(self.success_url)
		return super(AnimalFormView, self).post(self, form, **kwargs)
	
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
	success_url = '/animal/resumo'

	def post(self, form, **kwargs):
		if "cancel" in self.request.POST:
			self.object = self.get_object()
        		return HttpResponseRedirect(self.success_url)
		return super(AnimalEditar, self).post(self, form, **kwargs)

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
        
"""Classe para fazer a busca avancada dos atributos de animal"""
class AnimalBuscaAvancadaMixin(ListAnimal,FormView):
	form = AnimalBuscaAdvForm
	form_class = AnimalBuscaAdvForm
	template_name = 'cadastro/animal_resumo.html'
	#success_url = '/animal/busca/avancada'
	success_url = '/success/'
	
	query=Animal.objects.all()
	
	def get(request,*args):
		if request.method == 'POST':
			form = AnimalBuscaAdvForm(request.POST)
			i = 0
			while i < len(query):
				if ((form.nome == None) | (query[i].nome__icontains__form.nome)):
					if ((form.rg == None) | (query[i].rg__icontains__form.rg)): 
						if ((form.especie == None) | (query[i].especie__icontains__form.especie)): 	
							if ((form.tutor == None) | (query[i].tutor.nome__icontains__form.tutor)): 
								if ((form.raca == None) | (query[i].raca__icontains__form.raca)):
									if ((form.idade == None) | (query[i].idade__icontains__form.idade)): 
										if ((form.sexo == None) | (query[i].sexo__icontains__form.sexo)):  
											lista_retornavel += query[i]
				i = i+1		
					
				
		else:
			AnimalBuscaAdvForm()

		#return lista_retornavel
		return HttpResponseRedirect('/animal/resumo')
		#return HttpResponseRedirect(reverse('seila', kwargs={'pk': self.lista_retornavel.pk}))
		
	#def get_queryset(self):
		#return self.lista_retornavel
		        

#Views relacionadas à classe Consulta:

class ConsultaFormView(FormView):
	template_name = 'cadastro/consulta_form.html'
	form_class = ConsultaModelForm
	success_url = '/consulta/resumo'
	
	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/consulta/resumo')

class ConsultaDeleteView(DeleteView):
	model = Consulta
	success_url = '/success/'
	#success_url = reverse_lazy('consulta_resumo')

class ConsultaDetailView(DetailView):
	pk_url_kwarg = "consulta_id"
	model = Consulta

	def get_context_data(self, **kwargs):
		context = super (ConsultaDetailView, self).get_context_data(**kwargs)
		return context

class ConsultaUpdateView(UpdateView):
	form_class = ConsultaModelForm
	model = Consulta
	template_name_suffix = '_form_update'
	success_url = '/success/'

class ConsultaListView(ListView):
	model = Consulta    	
	paginate_by = 10 

class ConsultaResumo(ConsultaListView):
	template_name='cadastro/consulta_resumo.html'
	
	def get_context_data(self, **kwargs):
		context = super (ConsultaResumo, self).get_context_data(**kwargs)
		context['form'] = ConsultaBuscaAdvForm()
		return context	
	
		

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
	success_url = '/exame/resumo'
	
	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/exame/resumo')


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
	template_name_suffix = '_form_update'
	success_url = '/success/'

class ExameListView(ListView):
	model = Exame    	
	paginate_by = 10

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
	                       (Q(animal__icontains=q) for q in query_list))|
			reduce(operator.and_,
	                       (Q(tecnico__icontains=q) for q in query_list)) |
			reduce(operator.and_,
	                       (Q(veterinario__icontains=q) for q in query_list))
	            )
	
	        return result
"""Classe para fazer a busca avancada dos atributos de exame"""	        
class ExameBuscaAvancadaMixin(ListView,View):	        
	form = ExameBuscaAdvForm
	form_class = ExameBuscaAdvForm
	template_name = 'cadastro/laboratorio_detail.html'
	#success_url = '/success/'
	
	query=Exame.objects.all()
	

	def get(request,*args):
		if request.method == 'POST':
			form = ExameBuscaAdvForm(request.POST)
			i = 0
			while i < len(query):
				if ((form.animal == None) | (query[i].animal.nome__icontains__form.animal)):
					if ((form.veterinario == None) | (query[i].veterinario.nome__icontains__form.veterinario)): 
						if ((form.tutor == None) | (query[i].tutor.nome__icontains__form.tutor)): 
							if ((form.tecnico == None) | (query[i].tecnico.nome__icontains__form.tecnico)): 
								if ((form.laboratorio == None) | (query[i].laboratorio.nome__icontains__form.laboratorio)): 
									lista_retornavel += query[i]
				i = i+1		
					
		else:
			ExameBuscaAdvForm()

		return lista_retornavel
		#return HttpResponseRedirect('/exame/resumo')	        

#Views relacionadas à classe Laboratorio:

class LaboratorioListView(ListView):
	model = Laboratorio    	
	paginate_by = 10 

class LaboratorioResumo(LaboratorioListView):
	template_name='cadastro/laboratorio_resumo.html'
	

class LaboratorioDetailView(DetailView):
	pk_url_kwarg = "laboratorio_id"
	model = Laboratorio
	
	def get_context_data(self, **kwargs):
		context = super (LaboratorioDetailView, self).get_context_data(**kwargs)
		context['form'] = ExameBuscaAdvForm()
		return context	
	
	
