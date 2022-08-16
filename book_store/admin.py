from book_store.models import Author, Book, Publisher, Store

from django.contrib import admin


class BookInline(admin.StackedInline):
    model = Book
    extra = 1


class BooksInline(admin.StackedInline):
    model = Book.authors.through
    extra = 1


class StoreInline(admin.StackedInline):
    model = Store.books.through
    extra = 1


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [BookInline, ]


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'pages', 'price', 'rating', 'pubdate')
    inlines = [BooksInline, StoreInline, ]
    fieldsets = (
        (None, {
            'fields': ('name', 'pages', 'price')
        }),
        ('Rating', {
            'fields': ('rating',)
        }),
        ('Date', {
            'fields': ('pubdate',)
        }),
    )
    list_filter = ['rating', 'pubdate',]
    search_fields = ['name', 'rating']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [BooksInline]
    list_filter = ['age', 'book']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [StoreInline, ]
    list_filter = ['name']
    search_fields = ['name', ]
