from django.shortcuts import render, get_object_or_404
from .models import Book, Category

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    related_items = Book.objects.filter(author = book.author).exclude(pk=pk)[0:3]

    return render(request, 'books/detail.html', {
        'book': book,
        'related_items': related_items,
    })

