from django import forms

from .models import UploadedARLFile, UploadedEPSFile, UploadedLABORALFile, Semestres, Estudiante


class DatosForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    codigo = forms.CharField(max_length=10)
    correo = forms.EmailField()
    horas = forms.IntegerField()
    programa = forms.CharField(max_length=100, required=False)


class ProgramForm(forms.Form):
    codigo = forms.CharField(max_length=100)
    programa = forms.CharField(max_length=255)
    facultad = forms.CharField(max_length=100)


class SemestreForm(forms.Form):
    semestre = forms.CharField(max_length=100)
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()

class FileUploadARLForm(forms.ModelForm):
    class Meta:
        model = UploadedARLFile
        fields = ["file"]


class FileUploadEPSForm(forms.ModelForm):
    class Meta:
        model = UploadedEPSFile
        fields = ["file"]


class FileUploadLABORALForm(forms.ModelForm):
    class Meta:
        model = UploadedLABORALFile
        fields = ["file"]
