from django.urls import path
from .           import views

urlpatterns = [
    path('',            views.home,     name='home'),
    path('contact',     views.contact,  name='contact'),
    path('books',       views.books,    name='books'),
    path('books/add',   views.add,      name='add'),
    path('books/edit/<int:id>',  views.edit,     name='edit'),
    path('delete/<int:id>',  views.delete,     name='delete'), 
]