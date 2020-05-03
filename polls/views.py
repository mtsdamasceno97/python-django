from django.shortcuts import render, redirect
from .forms import Insertusuario
from django.http import HttpResponse
from .models import Usuario
# Create your views here.

def index(request):
  return HttpResponse("Hello, world")

def cadastrar(request):
  form = Insertusuario(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('index')
  return render(request,'cadastro.html',{'form':form})

def listar(request):
  usuarios = Usuario.objects.all() #retorna todas as linhas da tabela
  return render(request, 'listar.html', {'usuarios': usuarios})

def deletar(request, id):
  user = Usuario.objects.get(id = id)
  if request.method == POST:
    user.delete()
    return redirect('listar')
  return render(request, 'confirme.html', {'user': user})

  

  