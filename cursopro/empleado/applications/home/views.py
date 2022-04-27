from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
# import models
from .models import Prueba
from .forms import PruebaForm

#Mostrar archivos html:
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'

class HomeTemplate1View(TemplateView):
    template_name = 'home/home1.html'

class HomeTemplate2View(TemplateView):
    template_name = 'home/home2.html'

class HomeTemplate3View(TemplateView):
    template_name = 'home/home3.html'

#Listar objetos o registros de una base de datos:
class PruebaListView(ListView):
    #model = MODEL_NAME #BD
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30'] #hace referencia a una lista

class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'

#Crear un registro sobre un modelo de BD
class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'