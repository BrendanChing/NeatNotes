from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.
class SignupView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('login')
    success_message = "Welcome to NeatNotes! Please sign in with the details you just entered."

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)    

class LoginInterfaceView(SuccessMessageMixin, LoginView):
    template_name = 'home/login.html'
    success_message = "Welcome! You are logged in."

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'        

class HomeView(TemplateView):
    template_name = 'home/welcome.html'

