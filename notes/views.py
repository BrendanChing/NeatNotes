from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/neat/notes/'
    template_name = 'notes/notes_delete.html'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/neat/notes/'
    form_class = NotesForm
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/neat/notes/'
    form_class = NotesForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    login_url = "/login"
    template_name = "notes/notes_list.html"
    ordering = ['-created']

    def get_queryset(self):
        return self.request.user.notes.all().order_by(*self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate if there are any important notes
        has_important_notes = any(note.is_important for note in context['notes'])
        context['has_important_notes'] = has_important_notes
        return context


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

def toggle_important(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.is_important = not note.is_important
    note.save()
    return redirect('notes_detail', pk=pk)
