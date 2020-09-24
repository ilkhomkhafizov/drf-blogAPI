from django.views.generic import ListView

from .models import Book


class BooksListView(ListView):
    model = Book
    template_name = 'book_list.html'