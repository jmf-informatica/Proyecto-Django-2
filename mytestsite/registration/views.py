from django.shortcuts import render
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm, EmailForm
from django.urls import reverse_lazy
from .models import Profile
from django import forms
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    form_class=ProfileForm
    success_url=reverse_lazy('profile')
    template_name='registration/profile_form.html'
    login_url='login'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


class EmailUpdate(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    form_class=EmailForm
    success_url=reverse_lazy('profile')
    template_name='registration/profile_email_form.html'
    login_url='login'
    success_message = 'Su e-email fue modificado exitosamente'

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        
        # Modifica en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb2', 'placeholder':'Escriba su nuevo email'})
        return form


