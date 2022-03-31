from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Book
from .forms import BookForm

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')

# Book - CRUD
def books(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})
def add(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'books/create.html', {'form': form})
def edit(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('books')
    return render(request, 'books/edit.html', {'form': form}) 
def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')