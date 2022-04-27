from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import newDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento


class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name ='departamentos'

    

class newDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = newDepartamentoForm
    success_url = '/'

    def form_valid(self, form):

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa,
        )
        return super(newDepartamentoView, self).form_valid(form)