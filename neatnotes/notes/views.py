from django.shortcuts import render
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView

# Create your views here.
class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = '/smart/notes/'

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
