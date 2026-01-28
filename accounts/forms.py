from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe 
from .models import Profile

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    # Este bloque "estiliza" los cuadros de texto
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'Completar aquí...'
            })

        self.fields['username'].help_text = 'Obligatorio. Solo puede estar formado por letras, números y los caracteres @/./+/-/_.'

        # Usamos <br> para separar las líneas y mark_safe para que funcione
        self.fields['password1'].help_text = mark_safe(
            "• Debe tener al menos 8 caracteres.<br>"
            "• No puede ser solo números.<br>"
            "• Usá mayúsculas y minúsculas para más seguridad."
        )
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['imagen', 'descripcion', 'link']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, forms.FileInput): # No estiliza el botón de subir archivo
                field.widget.attrs.update({'class': 'form-control bg-dark text-white border-secondary'})

# Formulario para datos básicos (Nombre, Apellido, Email)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="Correo Electrónico")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control bg-dark text-white border-secondary mb-3'})

# Formulario para datos de Perfil (Imagen, Descripción, Link)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['imagen', 'descripcion', 'link']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # No le ponemos la clase form-control al archivo para que no se rompa el diseño
            if not isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({'class': 'form-control bg-dark text-white border-secondary mb-3'})

