from django.shortcuts import render
from .models import Author, Book, Genre, BookInstance

# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_instance': num_instance,
        'num_instances_available': num_instances_available
    }

    return render(request, 'index.html', context=context)
