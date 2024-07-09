from django.urls import path
from . import views

urlpatterns = [
    # Defines URL patterns for home, login, logout and signup. Each path maps to a specific view and has a name for easy reference.
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]