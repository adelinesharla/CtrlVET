# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

TIPO_CHOICES = (
		('Vet', 'Veterinário'),
		('Tec', 'Técnico'),
	)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='E-Mail')
    cpf = forms.CharField(label='CPF', max_length=11)
    tipo = forms.ChoiceField(label = 'Tipo', widget=forms.Select, choices=TIPO_CHOICES)
    registro = forms.CharField(label='CRMV/CRF', max_length=10)

    class Meta:
        model = User
        fields = ('username', 'email','cpf','tipo','registro', 'password1', 'password2', )
