from django.core.management.base import BaseCommand
from book_store.models import Author, Book, Publisher, Store
from faker import Faker
import random
from django.utils import timezone


class Command(BaseCommand):
    help = 'This command is for inserting Author, Book, Publisher, Store into database.Insert 10, Authors, ' \
           '10 Publishers, 100 Books, 10 Stores. '

    def handle(self, *args, **options):

        fake = Faker()
        # create 10 authors
        # authors = [Author(name=fake.name(), age=random.randint(18, 85)) for _ in range(500)]
        # Author.objects.bulk_create(authors)

        # # create 10 publishers
        # publishers = [Publisher(name=fake.company()) for _ in range(10)]
        # Publisher.objects.bulk_create(publishers)
        #
        # # create 10 books for every publishers
        # for publisher in Publisher.objects.all():
        #     for _ in range(20):
        #         books = [Book(name=fake.sentence(nb_words=3), pages=random.randint(25, 300),
        #                       price=round(random.uniform(15, 300), 1), rating=random.randint(1, 10),
        #                       pubdate=timezone.now(), publisher=publisher)]
        #
        #         Book.objects.bulk_create(books)
        #
        # author = Author.objects.all()
        # idd = []
        # for i in author:
        #     idd.append(i.pk)
        # for book in Book.objects.all():
        #     for y in range(1, 100):
        #         book.authors.add(author.get(id=random.choice(idd)))

        # create 10 stores and insert 10 books in every store
        # books = list(Book.objects.all())
        # for _ in range(10):
        #     temp_books = [books.pop(0) for _ in range(10)]
        #     store = Store.objects.create(name=fake.company())
        #     store.books.set(temp_books)
        #     store.save()
