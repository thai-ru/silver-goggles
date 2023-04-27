from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models
import uuid # Imoprtant for selecting unique user id for the book

# Create your models here.
class Genre(models.Model):

    name = models.CharField(max_length=200, help_text="Enter Genre e.g Programming, Fictional...")

    def __str__(self):
        return self.name
    
class Title(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book!1")
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.ManyToManyField(Genre, help_text='Select a Genre for this book')

    def __str__(self):
        return self.title

    def  get_absolute_url(self):
        
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Set unique text for BookInstance')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_finish = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
       ('m', 'Maintenance'),
       ('o', 'On loan'),
       ('a', 'Available'),
       ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
         ordering = ['due_finish']

    def __str__(self):
        return f'{self.id}, ({self.book.title})'