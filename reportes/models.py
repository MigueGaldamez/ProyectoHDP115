from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from departamentos.models import Departamento
from municipios.models import Municipio
    
class Reporte(models.Model):
	cantidadPruebas = models.IntegerField()
	cantidadPositivas = models.IntegerField()
	departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE) 
	municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE) 
	estado = models.IntegerField()
	class Meta:
		db_table="reporte"





