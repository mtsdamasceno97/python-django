from django.shortcuts import render, redirect
from .forms import Insertusuario
from django.http import HttpResponse
# Create your views here.

def index(request):
  return HttpResponse("Hello, world")

def cadastrar(request):
  form = Insertusuario(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('index')
  return render(request,'cadastro.html',{'form':form})