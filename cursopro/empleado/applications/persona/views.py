from django.shortcuts import render
from django.views.generic import (
ListView, DetailView, CreateView,
TemplateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
#models
from .models import Empleado
#forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'inicio.html'

# 1. Listar todos los empleados de la empresa

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


# 2. Listar todos los empleados que pertenecen a un área de la empresa
class ListByArea(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    #2.1. Mejor opción de listar
    def get_queryset(self):
        #el código que yo quiera
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
    )
        return lista

# 3. Listar empleados por trabajo
class ListByJob(ListView):
    template_name = 'persona/list_by_job.html'

    #2.1. Mejor opción de listar
    def get_queryset(self):
        #el código que yo quiera
        trabajo = self.kwargs['job']
        lista = Empleado.objects.filter(
        departamento__shor_name = trabajo
    )
        return lista

# 4. Listar los empleados por palabra clave
class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('*****************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

# 5. Listar habilidades de un empleado

class ListByHabilidades(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id='1')
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name =  "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    model = Empleado
    template_name = 'persona/success.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/add.html'
    fields = ['first_name', 'last_name', 'full_name' , 'job', 'departamento', 'habilidades', 'avatar',]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'persona/update.html'
    fields = ['first_name', 'last_name', 'full_name' , 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('***************METODO POST**************')
        print('****************************************')
        print('================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        print('***************METODO form valid**************')
        print('****************************************')
        return super().form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:empleados_admin')