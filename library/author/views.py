from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Author
from book.models import Book  # Assuming you have a Book model
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def is_librarian(user):
    return user.is_authenticated and user.role == 1


@login_required
def list_all_authors(request):
    if not is_librarian(request.user):
        return HttpResponseForbidden("You are not authorized to view this page.")
    authors = Author.objects.all()
    return render(request, 'author/list_authors.html', {'authors': authors})


@login_required
def create_author(request):
    if not is_librarian(request.user):
        return HttpResponseForbidden("You are not authorized to create authors.")
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        print(f"Name: {name}, Surname: {surname}, Patronymic: {patronymic}")
        if name:
            Author.objects.create(
                name=name, surname=surname, patronymic=patronymic)
            return redirect('all_authors')
    return render(request, 'author/create_author.html')


@login_required
def delete_author(request, author_id):
    if not is_librarian(request.user):
        return HttpResponseForbidden("You are not authorized to delete authors.")
    author = get_object_or_404(Author, pk=author_id)
    if author.books.exists():
        messages.error(request, 'You cannot delete this author')
        return redirect('all_authors')
    author.delete()
    messages.success(request, 'Author was successfully deleted')
    return redirect('all_authors')
