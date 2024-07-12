from django.urls import path
from . import views

""" 
urlpatterns that point to views based on the users
location on the site eg. 'notes/new'.
They are named for reference in urls and templates.
<int:pk> is used to identify
the users table in the database.
"""
urlpatterns = [
    path('notes/', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>/', views.NotesDetailView.as_view(), name="notes_detail"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
    path('notes/<int:pk>/toggle-important/', views.toggle_important, name='toggle_important'),
]
