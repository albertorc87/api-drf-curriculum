from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Experience(models.Model):
    """Work experience model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience')
    date_ini = models.DateTimeField()
    date_end = models.DateTimeField(null=True)
    company = models.CharField(max_length=255)
    description = RichTextField()


    def __str__(self):
        """Return company and first_name and last_name."""
        return f'{self.user.first_name} {self.user.last_name} | {self.company}'