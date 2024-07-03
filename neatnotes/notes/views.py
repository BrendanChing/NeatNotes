from django.shortcuts import render
from .models import Notes
from django.views.generic import ListView

# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"

def detail(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'notes/notes_detail.html', {'note': note})