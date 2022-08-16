from book_store import views

from django.urls import path

from django.views.decorators.cache import cache_page

app_name = 'book_store'

urlpatterns = [path('', cache_page(60*10)(views.index), name='index'),
               path('publisher/', views.publisher, name='publisher'),
               path('publisher/<int:publisher_id>', views.publisher_book, name='publisher_book'),
               path('author/', views.author, name='author'),
               path('author/<int:young_author>', views.author_book, name='author_book'),
               path('books_list/', views.books, name='books'),
               path('books_all/', views.books_all, name='books_all'),
               path('books_one/<int:ids>', views.books_one, name='books_one'),
               path('store/', views.store, name='store'),
               path('store_books/<int:store_id>', views.store_books, name='store_books'),

               path('authors/<int:pk>', cache_page(60*10)(views.AuthorDetailView.as_view()), name='author-detail'),
               path('authors/', cache_page(60*10)(views.AuthorListView.as_view()), name='author-list'),
               path('authors/create', views.AuthorCreateView.as_view(), name='author-create'),
               path('authors/<int:pk>/update', views.AuthorUpdateView.as_view(), name='author-update'),
               path('authors/<int:pk>/delete', views.AuthorDeleteView.as_view(), name='author-delete'),

               path('publishers/<int:pk>', cache_page(60*10)(views.PublisherDetailView.as_view()),
                    name='publisher-detail'),
               path('publishers/', cache_page(60*10)(views.PublisherListView.as_view()), name='publisher-list'),
               path('publishers/create', views.PublisherCreateView.as_view(), name='publisher-create'),
               path('publishers/<int:pk>/update', views.PublisherUpdateView.as_view(), name='publisher-update'),
               path('publishers/<int:pk>/delete', views.PublisherDetailView.as_view(), name='publisher-delete'),

               path('books/<int:pk>', cache_page(60*10)(views.BooksDetailView.as_view()), name='book-detail'),
               path('books/', cache_page(60*10)(views.BookListView.as_view()), name='book-list'),
               path('books/create', views.BooksCreateView.as_view(), name='book-create'),
               path('books/<int:pk>/update', views.BooksUpdateView.as_view(), name='book-update'),
               path('books/<int:pk>/delete', views.BooksDeleteView.as_view(), name='book-delete'),

               ]
