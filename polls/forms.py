from django.forms import ModelForm
from .models import Usuario

class Insertusuario(ModelForm):
  class Meta:
    model = Usuario
    fields = '__all__'