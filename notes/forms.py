from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-3'}),
        }
        labels = {
            'text': 'Write your note here'
        }
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if not title:
            # Extract the first three words from the text
            first_three_words = ' '.join(text.split()[:3])
            cleaned_data['title'] = first_three_words

        return cleaned_data
