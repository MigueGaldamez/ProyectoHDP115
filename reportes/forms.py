import json
from django import forms
from .models import Reporte
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from departamentos.models import Departamento
from municipios.models import Municipio
from perfiles.models import Perfil

class ReporteForm(forms.ModelForm):

	estado = forms.IntegerField(required=False)
	class Meta:
		model = Reporte
		fields =['cantidadPruebas','cantidadPositivas','departamento','municipio','estado']
	
	def __init__(self, *args , **kwargs):
		super().__init__(*args , **kwargs)
		self.fields['municipio'].queryset = Municipio.objects.none()

		if 'departamento' in self.data:
			try:
				departamento_id =int(self.data.get('departamento'))
				self.fields['municipio'].queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
			except(ValueError ,TypeError):
				pass 	
		
		elif self.instance.pk:
			self.fields['municipio'].queryset = self.instance.departamento.municipio_set.order_by('nombre')

