# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import url

"""Classes de views genericas utilizadas"""
from django.views.generic import View, TemplateView, DetailView, UpdateView, DeleteView,ListView,FormView

'Importando Formularios necessários'
from .forms import *

'Importando Models necessárias'
from .models import *

from django.forms.models import model_to_dict #iterar em object no template

'Importando atributos da model a serem utilizados nas buscas'
import operator
from django.db.models import Q
