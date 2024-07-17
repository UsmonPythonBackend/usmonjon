from django.shortcuts import render
from .models import Book, Author, Comments


def home(request):
    return render(request, 'home.html')

def books(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(title__icontains=search) | Book.objects.filter(author__first_name__icontains=search)
        if books:
            return render(request, 'books.html', {'books': books,   "value": search, "message": "Succesfully"})
        else:
            return render(request, 'books.html', {'message': "Not Found"})
        books = Book.objects.all()
    return render(request, 'books.html', {'books': books, "value": search})


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    if book:
        return render(request, 'book_detail.html', {'book': book, "message": "Succesfully"})
    else:
        return render(request, 'book_detail.html', {"message": "Not Found"})






def authors(request):
    if request.method == 'POST':
        search = request.POST['search']
        authors = Author.objects.filter(get_full_name__icontains=search)
        if authors:
            return render(request, 'authors.html', {'authors': authors, "value": search, "message": "Succesfully"})
        else:
            return render(request, 'authors.html', {'message': "Not Found"})
        authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors, "value": search})


def comments(request):
    comments = Comments.objects.all()
    return render(request, 'comments.html', {'comments': comments})





