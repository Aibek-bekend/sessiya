from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)

def book_detail(request, id):
    try:
        book = Book.objects.values().get(id=id)
        return JsonResponse(book, safe=False)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Книга не найдена'}, status=404)

from django.shortcuts import render
from .models import Book

def book_list_page(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})
    path('book_list/', book_list_page),
