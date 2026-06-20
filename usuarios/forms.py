import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@correo.com',
            'pattern': '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'title': 'Ingrese un correo válido.'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '********',
            # Ejemplo de Regex para contraseña fuerte (mínimo 8 chars, 1 mayus, 1 num)
            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\w\W]{8,}$',
            'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula y un número.'
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Sanitización: Restricción estricta de caracteres especiales para evitar inyecciones
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', username):
            raise ValidationError(_("El correo contiene caracteres no permitidos."))
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Validación de caracteres extraños que no deberían estar en una contraseña normal
        if re.search(r'[\'"\\]', password):
            raise ValidationError(_("La contraseña contiene caracteres no permitidos."))
        return password
