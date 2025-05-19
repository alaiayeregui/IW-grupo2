from django.shortcuts import redirect, render, get_object_or_404

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from .models import Cliente, Empleado, Tarea, Proyecto, Responsable, Documento
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView, FormView
from .forms import EmpleadoForm, ClienteForm, ProyectoForm, ResponsableForm, TareaForm, TareaNotasForm, DocumentoForm,  CorreoContactoForm

def index(request):
    return render(request, 'index.html')

#ver empleados
class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.all()

#detalles de un empleado
class EmpleadoDetailView(DetailView):
    model = Empleado

#crear un empleado
class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleados')

#eliminar un empleado
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

#actualizar datos de un empleado
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleados')

#ver clientes
class ClienteListView(ListView):
    model = Cliente

#detalles de un cliente
class ClienteDetailView(DetailView):
    model = Cliente

#crear un cliente nuevo
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

#actualizar información de un cliente
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

#detalles de un proyecto
class ProyectoDetailView(DetailView):
    model = Proyecto

#ver todos los proyectos
class ProyectoListView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.all()
    template_name = 'proyecto_list.html'

#crear un proyecto nuevo
class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('proyectos')

    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['auto_id'] = 'proyecto_%s' 
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doc_form'] = DocumentoForm(self.request.POST or None, self.request.FILES or None)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        doc_form = context['doc_form']
        self.object = form.save()

        if doc_form.is_valid() and doc_form.cleaned_data.get('documento'):
            documento = doc_form.save(commit=False)
            documento.proyecto = self.object
            documento.save()

        return super().form_valid(form)

#eliminar un proyecto
class ProyectoDeleteView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('proyectos')

#actualizar datos de un proyecto
class ProyectoUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('proyectos')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['auto_id'] = 'proyecto_%s' 
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doc_form'] = DocumentoForm(self.request.POST or None, self.request.FILES or None)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        doc_form = context['doc_form']
        self.object = form.save()

        if doc_form.is_valid() and doc_form.cleaned_data.get('documento'):
            documento = doc_form.save(commit=False)
            documento.proyecto = self.object
            documento.save()

        return super().form_valid(form)

#detalles de un responsable
class ResponsableDetailView(DetailView):
    model = Responsable

#ver todos los responsables
class ResponsableListView(ListView):
    model = Responsable
    queryset = Responsable.objects.all()

#añadir un responsable nuevo
class ResponsableCreateView(CreateView):
    model = Responsable
    form_class = ResponsableForm
    template_name = 'responsable_form.html'
    success_url = reverse_lazy('responsables')

#eliminar un responsable
class ResponsableDeleteView(DeleteView):
    model = Responsable
    success_url = reverse_lazy('responsables')

#actializar información de un responsable
class ResponsableUpdateView(UpdateView):
    model = Responsable
    form_class = ResponsableForm
    template_name = 'responsable_form.html'
    success_url = reverse_lazy('responsables')

#mostrar todas las tareas
class TareaListView(ListView):
    model = Tarea
    queryset = Tarea.objects.all()

#detalles de una tarea
class TareaDetailView(DetailView):
    model = Tarea

#añadir una nueva tarea
class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('tareas')

#eliminar una tarea
class TareaDeleteView(DeleteView):
    model = Tarea
    success_url = reverse_lazy('tareas')

#actualizar cualquier dato de una tarea
class TareaUpdateView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('tareas')

#actualizar el campo de notas de una tarea
class TareaNotasUpdateView(UpdateView):
    model = Tarea
    form_class = TareaNotasForm  # solo el campo 'notas'
    template_name = 'tarea_notas_form.html'
    success_url = reverse_lazy('tareas')

#filtrado de tareas por la prioridad y estado
def buscarTarea(request):
    prioridad = request.GET.get('prioridad', '')
    estado = request.GET.get('estado', '')
    tareas = Tarea.objects.all()

    if prioridad:
        tareas = tareas.filter(prioridad=prioridad)
    if estado:
        tareas = tareas.filter(estado=estado)

    context = {
        'tareas': tareas,
        'prioridad': prioridad,
        'estado': estado,
    }

    return render(request, 'buscar_tareas.html', context)


#enviar emails de contacto
class ContactoEmailView(FormView):
    template_name = 'correo_form.html'
    form_class = CorreoContactoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        correo = form.cleaned_data['correo']
        asunto = form.cleaned_data['asunto']
        mensaje = form.cleaned_data['mensaje']

        mensaje_completo = f"De: {nombre} <{correo}>\n\n{mensaje}"

        send_mail(
            asunto,
            mensaje_completo,
            'grupo2e3y4@gmail.com',
            ['grupo2e3y4@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)

