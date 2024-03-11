from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView
from django.views.generic import DetailView
from .models import Registration
from django.views.generic import FormView, DetailView

from .models import Registration


# Create your views here.
from django import forms
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone_number', 'gender', 'password', 'confirm_password']

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm  # Use the RegistrationForm class
    success_url = reverse_lazy('task-create')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskUpdate(UpdateView):
    model = Registration
    fields = ['name','email','phone_number','gender','password','confirm_password']
    template_name = 'register.html'
    success_url = reverse_lazy('registration-detail')


class RegistrationDetailView(DetailView):
    model = Registration
    template_name = 'taskdetail.html'
