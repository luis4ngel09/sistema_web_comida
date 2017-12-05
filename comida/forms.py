from django import forms
from .models import comidas,pedidos, usuarios

class comidaForm(forms.ModelForm):
	class Meta:
		model = comidas
		fields=('nombre','descripcion','costo','fecha_creacion','imagen',)

class pedidoForm(forms.ModelForm):
	class Meta:
		model= pedidos
		fields=('comida_id','nombre','cantidad','descripcion','fecha_creacion')

class usuarioForm(forms.ModelForm):
	class Meta:
		model= usuarios
		fields=('nombre','password')