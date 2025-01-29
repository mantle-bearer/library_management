from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    availability = models.CharField(max_length=20, default='available')
    edition = models.CharField(max_length=50, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
