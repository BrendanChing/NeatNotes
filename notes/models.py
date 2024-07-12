from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    """
    A model to represent notes created by users and define
    the structure of the Notes table in the database.

    Notable Fields:
    - created: DateTimeField automatically set to
               current time on creation, used for
               ordering of notes.
    - user: ForeignKey to User model with CASCADE
            delete behavior, which deletes all related
            data when the user is deleted.
    - is_important: BooleanField to indicate whether
            the note is marked as important by the user.
    """
    title = models.CharField(max_length=70)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes'
    )
    is_important = models.BooleanField(default=False)

    def __str__(self):
        # Returns the title of the note as its string representation
        return self.title
