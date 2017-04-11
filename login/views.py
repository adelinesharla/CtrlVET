from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from cadastro.models import Veterinario, Tecnico
from forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user = User.objects.get(username=username)
            if form.cleaned_data.get('tipo') == 'Tec':
            	tec = Tecnico(nome=form.cleaned_data.get('username'), email=form.cleaned_data.get('email'), cpf=form.cleaned_data.get('cpf'), crf=form.cleaned_data.get('registro'))
            	tec.save()
		group = Group.objects.get(name='Tecnico')
		user.groups.add(group)
            else:
            	vet = Veterinario(nome=form.cleaned_data.get('username'), email=form.cleaned_data.get('email'), cpf=form.cleaned_data.get('cpf'), crmv=form.cleaned_data.get('registro'))
            	vet.save()
		group = Group.objects.get(name='Veterinario')
		user.groups.add(group)
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
