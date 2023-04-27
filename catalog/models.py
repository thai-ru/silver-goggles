from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models
import uuid # Imoprtant for selecting unique user id for the book

# Create your models here.
class Genre(models.Model):

    name = models.CharField(max_length=200, help_text="Enter Genre e.g Programming, Fictional...")

    def __str__(self):
        return self.name
    
class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book!1")
    year = models.DateField(null=True, blank=True)
    edition = models.CharField(max_length=200, help_text='What edition is the book e.g 1\'st edition', null= True, blank=True)


    genre = models.ManyToManyField(Genre, help_text='Select a Genre for this book')

    def __str__(self):
        return self.title

    def  get_absolute_url(self):
        
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description= 'Genre'

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
         ordering = ['-due_finish']

    def __str__(self):
        return f'{self.id}, ({self.book.title})'

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
  
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'