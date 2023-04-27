from django.contrib import admin
from .models import Author, Genre, Book, BookInstance
# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book

#Author admin model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'year')
    fields = ['first_name', 'last_name', ('year', 'edition')]
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

#Book Admin model

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    inlines = [BooksInstanceInline]

admin.site.register(Book, BookAdmin)

#BookInstance admin model

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):

    list_display = ('book', 'status', 'due_finish', 'id')
    list_filter = ('status', 'due_finish')


    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_finish')
        }),
    )