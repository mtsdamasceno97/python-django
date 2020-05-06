from django.urls import path
from . import views

urlpatterns =[
  path('', views.index, name='index'),
  path('index', views.index, name='index'),
  path('cadastrar', views.cadastrar, name='cadastrar'),
  path('listar', views.listar, name='listar'),
  path('deletar/<int:id>', views.deletar, name='deletar'),
  path('alterar/<int:id>', views.alterar, name='alterar')

]

