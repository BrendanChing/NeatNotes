from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    """
    Form for creating a note
    """
    class Meta:
        model = Notes
        fields = ('title', 'text')
        # Widgets for adding django's form control which controls valid input, display and error messages
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-3'}),
        }
        labels = {
            # Placeholder text for text feild
            'text': 'Write your note here'
        }

    # Override init to set title field to not required
    def __init__(self, *args, **kwargs):
        """ 
        Calls the parent class (forms.Modelform) with super() then passes arguments from NotesForm into it.
        Then overrides the title required attribute, setting it to false. This is to allow no title input from
        the user and instead fill the title with the first 3 words of the content.
        """
        super().__init__(*args, **kwargs) 
        self.fields['title'].required = False    

    def clean(self):
        # Ensures data passed if the input is valid
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        # Ensures text is not None or empty
        if text:
            # Extract the first three words from the text
            first_three_words = ' '.join(text.split()[:3])
            # Set title to the first three words if title is empty
            if not title:
                cleaned_data['title'] = first_three_words

        return cleaned_data
