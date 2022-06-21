from django.db import models
from django.forms import CharField

class Funcionarios(models.Model):
  nome=CharField(max_length=100,)
  
  
  
  def __str__(self):
    return self.nome