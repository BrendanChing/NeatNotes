from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

class SignupView(SuccessMessageMixin, CreateView):
    """
    Signup view: handles user registration.
    """
    form_class = UserCreationForm       # links view to form for creating users
    template_name = 'home/register.html'
    success_url = reverse_lazy('login')     # Use reverse_lazy to defer URL resolution until runtime, and makes sure all URL patterns are loaded 
    success_message = "Welcome to NeatNotes! Please sign in with the details you just entered." # Built in django attribute to display a success message on home/registration.html

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests: redirects authenticated users to the notes list.

        Args are passed to allow passing of primary keys.
        kwargs are passed to allow query parameters.
        """
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)    

class LoginInterfaceView(SuccessMessageMixin, LoginView):
    """ 
    Login view to send the user from the login page to the home page and display success message.
    """
    template_name = 'home/login.html'
    success_message = "Welcome! You are logged in."

class LogoutInterfaceView(LogoutView):
    """ 
    Sends user to logout page. Note: there is no success message as it is already in the HTML page.
    """
    template_name = 'home/logout.html'        

class HomeView(TemplateView):
    """ 
    Sends user to home page.
    """
    template_name = 'home/welcome.html'

