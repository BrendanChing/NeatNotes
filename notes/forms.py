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

    # Override init to set title field to not required
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = False    

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        # Ensure text is not None or empty
        if text:
            # Extract the first three words from the text
            first_three_words = ' '.join(text.split()[:3])
            # Set title to the first three words if title is empty
            if not title:
                cleaned_data['title'] = first_three_words

        return cleaned_data
