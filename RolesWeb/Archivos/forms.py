from django import forms


class DatosForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    codigo = forms.CharField(max_length=10)
    correo = forms.EmailField()
    horas = forms.IntegerField()
    programa = forms.CharField(max_length=100)
