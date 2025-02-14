from django.views import generic
from django.shortcuts import render, get_object_or_404

from .models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    books_contain_a = Book.objects.all().filter(title__icontains='a').count()

    genres_contain_fiction = Genre.objects.all().filter(
        name__icontains='fiction').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances, 
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'Books_a': books_contain_a,
        'Genres': genres_contain_fiction
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'catalog/book_detail.html', context={'book': book})

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

def author_detail_view(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'catalog/author_detail.html', context={'author': author})


# Create your views here.
