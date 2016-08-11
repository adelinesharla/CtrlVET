from django.shortcuts import render
from django.conf.urls import url
'HttpResponse para uma pagina template indicando que a operação foi realizada (verificar se tal página existe)'
from django.http import HttpResponseRedirect
'Imortando Formularios necessários para views de tutor e animal'
from .forms import TutorModelForm, AnimalModelForm


'TUTOR FORM VIEW , PARA FORMULARIO DE CADASTRO DO TUTOR'
class TutorFormView(View):
  form_class_tutor = TutorModelForm
  template_formulario = 'form.html'
  
  def get(self, request):
    form = self.form_class()
    return render(request, self.template_formulario, {'form':form})
  
  def post(self, request):
    form = self.form_class(request.POST)
    if form.is_valid():
      return HttpResponseRedirect('/success/')
    
    return render(request, self.template_formulario, {'form':form})
'ANIMAL FORM VIEW, PARA FORMULARIO DE CADASTRO DO ANIMAL'    
class AnimalFormView(View):
  form_class_animal = AnimalModelForm
  template_formulario = 'form.html'
  
  def get(self, request):
    form = self.form_class()
    return render(request, self.template_formulario, {'form':form})
  
  def post(self, request):
    form = self.form_class(request.POST)
    if form.is_valid():
      return HttpResponseRedirect('/success/')
    
    return render(request, self.template_formulario, {'form':form})
    
    
# Create your views here.
