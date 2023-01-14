from django.shortcuts import get_object_or_404, redirect, render
from django.forms import ModelForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

@login_required(login_url='/login/')
def logout_user(request):
    if request.POST:
        print("estou aqui no logout")
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')


def login_user(request):
    print('estou em login user')
    if request.POST:
        print('cheguei aqui')
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        usuario_authentic = authenticate(username=usuario, password=senha)
        if usuario_authentic is not None:
            login(request, usuario_authentic)
            return redirect('lista_pessoas')
    return render(request, 'login.html')


class Formulario_Cadastro(ModelForm):
    class Meta:
        model = Proprietario
        fields = ['nome', 'email', 'sexo', 'nome_carro', 'modelo', 'cor']



@login_required(login_url='/login/')
def lista_pessoas(request, template_name='lista_pessoas.html'):
    Cadastro = Proprietario.objects.all()

    cadastrados = {'lista': Cadastro}

    return render(request, template_name, cadastrados)


@login_required(login_url='/login/')
def cadastro(request, template_name='cadastro_pessoas.html'):
    form = Formulario_Cadastro(request.POST or None)
    Cadastro = Proprietario.objects.all()
    if form.is_valid():
        form.save()
        return redirect('lista_pessoas')
    return render(request, template_name, {'form': form})



@login_required(login_url='/login/')
def editar_cadastro(request, pk, template_name='cadastro_pessoas.html'):
    pessoa = get_object_or_404(Proprietario, pk=pk)
    if request.method == "POST":
        form = Formulario_Cadastro(request.POST, instance=pessoa)
        if form.is_valid():
            pessoa = form.save()
            return redirect('lista_pessoas')
    else:

        form = Formulario_Cadastro(request.POST or None, instance=pessoa)
    return render(request, template_name, {'form': form})


@login_required(login_url='/login/')
def remover_pessoa(request, pk):
    pessoa = Proprietario.objects.get(pk=pk)
    if request.POST:
        pessoa.delete()
        return redirect('lista_pessoas')

    return render(request, 'pessoa_delete.html', {'pessoa': pessoa})


