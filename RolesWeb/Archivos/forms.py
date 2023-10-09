from django import forms


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
