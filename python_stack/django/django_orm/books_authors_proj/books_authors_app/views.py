from django.shortcuts import render, redirect
from books_authors_app.models import *
# Create your views here.
def books(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'Books.html', context)

def create_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['description']
        )
    return redirect('/books')

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        "book": book,
        "authors": Author.objects.exclude(books=book)
    }
    return render(request, 'Book_Detail.html', context)

def add_author_to_book(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        author = Author.objects.get(id=request.POST['author_id'])
        book.authors.add(author)
    return redirect(f'/books/{book_id}/')

def authors(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, 'Authors.html', context)

def create_author(request):
    if request.method == "POST":
        Author.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            notes=request.POST['notes']
        )
    return redirect('/authors/')

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
        "books": Book.objects.exclude(authors=author)
    }
    return render(request, 'Author_Detail.html', context)

def add_book_to_author(request, author_id):
    if request.method == "POST":
        author = Author.objects.get(id=author_id)
        book = Book.objects.get(id=request.POST['book_id'])
        author.books.add(book)
    return redirect(f'/authors/{author_id}/')