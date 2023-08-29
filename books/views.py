from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category, Commment
from .forms import CommentForm

@login_required
def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    related_items = Book.objects.filter(author = book.author).exclude(pk=pk)[0:3]
    comments = Commment.objects.filter(book = book)
    # comments = Commment.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_by = request.user
            comment.book = book
            comment.save()

            return redirect("books:detail", pk=pk)

    else:
        form = CommentForm()

    return render(request, 'books/detail.html', {
        'book': book,
        'related_items': related_items,
        'form': form,
        'comments': comments
    })

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Commment, pk=pk,created_by = request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            form.save()
            return redirect('books:detail', pk=comment.book.id)
        
    else:
        form = CommentForm(instance=comment)

    return render(request, 'books/edit_comment.html', {
        'form': form,
        'title': 'Edit Comment',
    })   

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Commment, pk=pk, created_by = request.user)
    comment.delete()

    return redirect('books:detail', pk=comment.book.id)