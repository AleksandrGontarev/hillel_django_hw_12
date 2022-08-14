from .views import Index, AuthorDetailView, AuthorListView, AuthorCreateView
from book_store import views

from django.urls import path

app_name = 'book_store'

urlpatterns = [path('', views.index, name='index'),
               path('publisher/', views.publisher, name='publisher'),
               path('publisher/<int:publisher_id>', views.publisher_book, name='publisher_book'),
               path('author/', views.author, name='author'),
               path('author/<int:young_author>', views.author_book, name='author_book'),
               path('books/', views.books, name='books'),
               path('books_all/', views.books_all, name='books_all'),
               path('books_one/<int:ids>', views.books_one, name='books_one'),
               path('store/', views.store, name='store'),
               path('store_books/<int:store_id>', views.store_books, name='store_books'),
               path('example/', Index.as_view(), name='example'),
               path('authors/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
               path('authors/', AuthorListView.as_view(), name='author-list'),
               path('authors/create', AuthorCreateView.as_view(), name='author-create'),
               path('person_home/', views.person_home, name='person_home'),
               path('authors/<int:pk>/update', views.AuthorUpdate.as_view(), name='author-update'),
               path('authors/<int:pk>/delete', views.AuthorDelete.as_view(), name='author-delete'),

               ]
