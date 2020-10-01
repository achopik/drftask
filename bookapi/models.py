from django.db import models


class Book(models.Model):
    """
    A book-representing model
    """

    # ID field (Primary key of a table)
    id = models.AutoField(primary_key=True)

    # Title of the book
    title = models.CharField(max_length=255)

    # Name of the author
    author_name = models.CharField(max_length=255)

    # Description field
    description = models.TextField()

    def __str__(self):
        return f"{self.id} {self.title} by {self.author_name}"

