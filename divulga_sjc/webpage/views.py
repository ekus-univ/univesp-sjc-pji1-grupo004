from django.shortcuts import render
from .models import Negocio
from .forms import NegocioCreateForm
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    	return render(request, 'webpage/home.html', {})

class NegocioCreate(CreateView):
	model = Negocio
	form_class = NegocioCreateForm
	template_name = "webpage/negocio_create_form.html"