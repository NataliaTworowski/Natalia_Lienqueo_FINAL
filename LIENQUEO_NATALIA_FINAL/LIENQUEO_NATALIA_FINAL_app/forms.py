from django import forms
from .models import Inscrito, Institucion
from django.core import validators

class InscritoForm(forms.ModelForm):
    ESTADOS = [
        ('RESERVADO', 'Reservado'), 
        ('COMPLETADA', 'Completada'), 
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten')
    ]

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=80,
        error_messages={'max_length': 'El nombre no puede superar los 80 caracteres.'}
    )
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[validators.MinLengthValidator(8)]  
    )
    fecha_inscripcion = forms.DateField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'date'})
    )
    hora_inscripcion = forms.TimeField(
        widget=forms.TimeInput(attrs={'class': 'form-control','type':'time'})

    )
    estado = forms.ChoiceField(
        choices=ESTADOS,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    observacion = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Inscrito
        fields = ['nombre', 'telefono', 'fecha_inscripcion', 'institucion', 'hora_inscripcion', 'estado', 'observacion']
        

class InstitucionForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=100,
        error_messages={'max_length': 'El nombre no puede superar los 100 caracteres.'}
    )
    class Meta:
        model = Institucion
        fields = ['nombre']
