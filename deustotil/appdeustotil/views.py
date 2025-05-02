from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from .models import Cliente, Empleado, Tarea, Proyecto
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from .forms import EmpleadoForm, ClienteForm, ProyectoForm

def index(request):
    return render(request, 'index.html')

class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.all()

class EmpleadoDetailView(DetailView):
    model = Empleado

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleados')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleados')

class ClienteListView(ListView):
    model = Cliente

class ClienteDetailView(DetailView):
    model = Cliente

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

class ProyectoDetailView(DetailView):
    model = Proyecto

class ProyectoListView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.all()

class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('proyectos')

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('proyectos')

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('proyectos')