from django.shortcuts import render

from .models import Genre, Book


def genres(request):
    return{
        'genres': Genre.objects.all()
    }


def all_books(request):
    books = Genre.objects.all()
    return render(request, 'store/home.html', {'books': books})