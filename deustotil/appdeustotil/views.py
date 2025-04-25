from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from .models import Cliente, Empleado, Tarea, Proyecto
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from .forms import EmpleadoForm



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
