from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class SignUp(LoginRequiredMixin, CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
