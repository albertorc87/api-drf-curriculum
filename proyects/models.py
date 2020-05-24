from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Proyect(models.Model):
    """Proyect model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.URLField(null=True)
    description = RichTextField()


    def __str__(self):
        """Return proyect title and first_name and last_name."""
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'