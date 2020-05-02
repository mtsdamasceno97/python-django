from django.db import models

# Create your models here.

class Usuario(models.Model):

  #nome
  nome = models.CharField(
    max_length = 100
  )

  #sobronome
  sobrenome = models.CharField(
    max_length = 100
  )

  sexo_Choices = [
    ('F', 'Feminino'),
    ('M', 'Masculino')
  ]

  sexo = models.CharField(
    max_length = 100,
    choices = sexo_Choices
  )