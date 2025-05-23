from django import forms
from .models import Empleado, Cliente, Proyecto, Responsable, Tarea, Documento

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = '__all__'

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

class TareaNotasForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['notas']

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['titulo', 'documento']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].required = False
        self.fields['documento'].required = False

class CorreoContactoForm(forms.Form):
    nombre = forms.CharField()
    correo = forms.EmailField()
    asunto = forms.CharField(max_length=50)
    mensaje = forms.CharField(widget=forms.Textarea)
