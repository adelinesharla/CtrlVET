# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import url
from django.views.generic import View, TemplateView, DetailView, UpdateView, DeleteView,ListView
'HttpResponse para uma pagina template indicando que a operação foi realizada (verificar se tal página existe)'
from django.http import HttpResponseRedirect
'Importando Formularios necessários para views de tutor e animal'
from .forms import TutorModelForm, AnimalModelForm
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
	
"""Classe para listar os tutores"""
class ListTutor(ListView):
	model = TutorEndTel
	#tutor_list = Tutor.objects.all()
	#paginator = Paginator(tutor_list, 10)
	paginate_by = 10 
	#page = request.GET.get('page')
	#try:
		#tutores = paginator.page(page)
	#except PageNotAnInteger:
	#	tutores = paginator.page(1)
	#except EmptyPage:
	#	tutores = paginator.page(paginator.num_pages)
	#return render(request, 'tutor_resumo.html', {'tutores': tutores})
    
"""Classe para listar os animais"""    
class ListAnimal(ListView):
	model = Animal    	
	#animal_list = Animal.objects.all()
	#paginator = Paginator(animal_list, 10) 
	paginate_by = 10 
	#page = request.GET.get('page')
	#try:
		#animais = paginator.page(page)
	#except PageNotAnInteger:
		#animais = paginator.page(1)
	#except EmptyPage:
	#	animais = paginator.page(paginator.num_pages)
	#return render(request, 'animal_resumo.html', {'animais': animais})		
			

"""Classe de renderização do painel de tutor (sem contexto)"""
class TutorResumo(ListTutor):
	template_name='cadastro/tutor_resumo.html'

"""Classe de renderização do painel de tutor (sem contexto)"""
class AnimalResumo(ListAnimal):
	template_name='cadastro/animal_resumo.html'

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
