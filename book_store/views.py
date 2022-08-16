from book_store.models import Author, Book, Publisher, Store

from django.db.models import Avg, Count, Min
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import MultipleObjectMixin


def index(request):
    return render(request, "book_store/index.html")


def admin_panel(request):
    return render(request, "book_store/")


def publisher(request):
    pub_count = Publisher.objects.count()
    pub = Book.objects.select_related('publisher')

    return render(
        request,
        "book_store/publisher.html",
        {"pubs": pub,
         'pub_count': pub_count,
         }
    )


def publisher_book(request, publisher_id):
    publik = Book.objects.select_related('publisher')
    pub = publik.filter(publisher_id=publisher_id)

    return render(
        request,
        "book_store/publisher_book.html",
        {"books": pub,
         }
    )


def author(request):
    authors_count = Author.objects.prefetch_related('authors').count()
    young_author = Author.objects.all().aggregate(Min('age'))

    return render(
        request,
        "book_store/author.html",
        {"author": authors_count,
         "young_author": young_author,
         }
    )


def author_book(request, young_author):
    queryset = Author.objects.prefetch_related('book_set')
    authors = []
    for author1 in queryset:
        books = [book.name for book in author1.book_set.all()]
        if author1.age == young_author:
            authors.append({
                'id': author1.id, 'name': author1.name, 'books': books,

            })

    return render(
        request,
        "book_store/author_book.html",
        {"author_books": authors,

         }
    )


def books(request):
    book = Book.objects.count()
    return render(
        request,
        "book_store/books.html",
        {"book": book,

         }
    )


def books_all(request):
    books = Book.objects.all()
    return render(
        request,
        "book_store/books_all.html",
        {"books": books,
         }
    )


def books_one(request, ids):
    queryset = Book.objects.prefetch_related('authors')
    books = []
    for book in queryset:
        authors = [author.name for author in book.authors.all()]
        if book.id == ids:
            books.append({
                'id': book.id, 'name': book.name, 'authors': authors,
                'price': book.price, 'pages': book.pages, 'rating': book.rating,
                'pubdate': book.pubdate, 'publisher': book.publisher
            })

    return render(
        request,
        "book_store/books_one.html",
        {
            "book": books,
        }
    )


def store(request):
    pop = Store.objects.annotate(number_of_books=Count('books__name'), average_price=Avg('books__price'))

    return render(
        request,
        "book_store/store.html",
        {
            'pop': pop,
        }
    )


def store_books(request, store_id):
    queryset = Store.objects.prefetch_related('books')
    stores = []
    for store in queryset:
        books = [book for book in store.books.all()]
        if store.id == store_id:
            stores.append({
                'id': store.id, 'name': store.name, 'books': books,

            })

    return render(
        request,
        "book_store/store_books.html",
        {
            'stores': stores,
        }
    )


class AuthorDetailView(DetailView, MultipleObjectMixin):
    model = Author
    paginate_by = 10

    def get_context_data(self, **kwargs):
        object_list = Book.objects.filter(authors=self.get_object())
        context = super(AuthorDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class AuthorListView(ListView):
    model = Author
    paginate_by = 10
    ordering = ['name']


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name', 'age']


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['name', 'age']
    template_name = "book_store/author_update.html"


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy("book_store:author-list")
    success_message = 'Author Delete Successfully'
    template_name = "book_store/author_delete.html"


class PublisherDetailView(DetailView):
    model = Publisher


class PublisherListView(ListView):
    model = Publisher
    paginate_by = 10
    ordering = ['name']


class PublisherCreateView(CreateView):
    model = Publisher
    fields = ['name']


class PublisherUpdateView(UpdateView):
    model = Publisher
    fields = ['name']
    template_name = "book_store/publisher_update.html"


class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = reverse_lazy("book_store:publisher-list")
    success_message = 'Publisher Delete Successfully'
    template_name = "book_store/publisher_delete.html"


class BooksDetailView(DetailView):
    model = Book


class BookListView(ListView):
    model = Book
    paginate_by = 50
    ordering = ['name']
    queryset = Book.objects.select_related("publisher")


class BooksCreateView(CreateView):
    model = Book
    fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']


class BooksUpdateView(UpdateView):
    model = Book
    fields = ['name']
    template_name = "book_store/publisher_update.html"


class BooksDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("book_store:book-list")
    success_message = 'Book Delete Successfully'
    template_name = "book_store/book_delete.html"
