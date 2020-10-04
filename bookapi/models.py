from django.db import models


class Book(models.Model):
    """
    A book-representing model
    """

    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.title} by {self.author_name}"

