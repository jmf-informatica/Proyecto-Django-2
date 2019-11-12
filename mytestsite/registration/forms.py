from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['avatar','bio']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Escribe algo sobre ti'}),
        }

class EmailForm(forms.ModelForm):
    email=forms.EmailField(required=True,help_text='requerido 254 caracteres como maximo y debe ser un email valido'),
    
    class Meta:
        model=User
        fields=[
            'email'
        ]
        labels={'email':''}
    
    def clean_email(self): # Validacion del campo email.
        # Función que verifica si el email ya se encuentra registrado en la DB
        email=self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Este email ya se encuentra registrado.')
        return email
