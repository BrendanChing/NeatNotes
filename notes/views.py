from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class NotesDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    View to handle the deletion of a note.
    Ensures the user is logged in and shows a success message upon deletion.
    """
    model = Notes
    success_url = reverse_lazy('notes.list')
    template_name = 'notes/notes_delete.html'
    login_url = "/login"
    success_message = "Successfully deleted note."

    def get_queryset(self):
        """
        Return only the notes belonging to the logged-in user.
        """
        return self.request.user.notes.all()


class NotesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View to handle the updating of a note.
    Ensures the user is logged in and shows a success message upon update.
    """
    model = Notes
    success_url = reverse_lazy('notes.list')
    form_class = NotesForm
    login_url = "/login"
    success_message = "Successfully updated note."

    def get_queryset(self):
        """
        Return only the notes belonging to the logged-in user.
        """
        return self.request.user.notes.all()


class NotesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View to handle the creation of a new note.
    Ensures the user is logged in and shows a success message upon creation.
    """
    model = Notes
    success_url = reverse_lazy('notes.list')
    form_class = NotesForm
    login_url = "/login"
    success_message = "Successfully created note."

    def form_valid(self, form):
        """
        Set the user of the note to the logged-in user before saving the form.
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    """
    View to display a list of notes for the logged-in user.
    Orders the notes by creation date and passes a flag indicating if any notes are marked as important.
    """
    model = Notes
    context_object_name = "notes"
    login_url = "/login"
    template_name = "notes/notes_list.html"
    ordering = ['-created']

    def get_queryset(self):
        """
        Return the notes belonging to the logged-in user, ordered by creation date.
        """
        return self.request.user.notes.all().order_by(*self.ordering)

    def get_context_data(self, **kwargs):
        """
        Add a flag to the context indicating if there are any important notes.
        """
        context = super().get_context_data(**kwargs)
        # Calculate if there are any important notes
        has_important_notes = any(note.is_important for note in context['notes'])
        context['has_important_notes'] = has_important_notes
        return context    


class NotesDetailView(LoginRequiredMixin, DetailView):
    """
    View to display the details of a specific note.
    Ensures the user is logged in and retrieves the note belonging to the user.
    """
    model = Notes
    context_object_name = "note"
    login_url = "/login"

    def get_queryset(self):
        """
        Return only the notes belonging to the logged-in user.
        """
        return self.request.user.notes.all()

def toggle_important(request, pk):
    """
    Toggle the importance of a note.
    Retrieves the note by primary key (pk), toggles its importance status, and redirects to the note detail page.
    """
    note = get_object_or_404(Notes, pk=pk)
    note.is_important = not note.is_important
    note.save()
    return redirect('notes_detail', pk=pk)
