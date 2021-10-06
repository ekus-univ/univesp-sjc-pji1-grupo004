from django.shortcuts import render
from .models import Categoria, Negocio
from .forms import NegocioCreateForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
	template_name = "webpage/home.html"

	def get_context_data(self):
		context = super().get_context_data()
		context["categorias"] = Categoria.objects.all()
		return context

class NegocioCreate(CreateView):
	model = Negocio
	form_class = NegocioCreateForm
	template_name = "webpage/negocio_create_form.html"

class Categoria1List(TemplateView):
	template_name = "webpage/categoria1.html"

	def get_context_data(self):
		context = super().get_context_data()
		context["categorias"] = Categoria.objects.all()
		context["negocios"] = Negocio.objects.filter(categoria=1)
		return context

class Categoria2List(TemplateView):
	template_name = "webpage/categoria2.html"

	def get_context_data(self):
		context = super().get_context_data()
		context["categorias"] = Categoria.objects.all()
		context["negocios"] = Negocio.objects.filter(categoria=2)
		return context