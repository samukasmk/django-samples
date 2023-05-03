from django.core.management.base import BaseCommand
from samples.django_querys.models import Book
from samples.django_querys.decorators import query_debugger
from pprint import pprint


class Command(BaseCommand):
    """
    This command is for inserting Publisher, Book, Store into database.
    Insert 5 Publishers, 100 Books, 10 Stores.
    """

    def handle(self, *args, **options):
        self.book_list_select_related()

    @query_debugger
    def book_list_select_related(self):

        queryset = Book.objects.select_related('publisher').defer('publisher__age').all()

        books = []

        for book in queryset:
            books.append({'id': book.id, 'name': book.name,
                          'publisher_name': book.publisher.name})

        print(f'\nBooks objects ({len(books)}):')
        pprint(books)
        print()

        return books

"""
$ ./manage.py select_related_enabled_defer

Books objects (100):
[{'id': 1, 'name': 'Book1', 'publisher_name': 'Publisher1'},
 {'id': 2, 'name': 'Book2', 'publisher_name': 'Publisher1'},
 {'id': 3, 'name': 'Book3', 'publisher_name': 'Publisher1'},
 {'id': 4, 'name': 'Book4', 'publisher_name': 'Publisher1'},
 {'id': 5, 'name': 'Book5', 'publisher_name': 'Publisher1'},
 {'id': 6, 'name': 'Book6', 'publisher_name': 'Publisher1'},
 {'id': 7, 'name': 'Book7', 'publisher_name': 'Publisher1'},
 {'id': 8, 'name': 'Book8', 'publisher_name': 'Publisher1'},
 {'id': 9, 'name': 'Book9', 'publisher_name': 'Publisher1'},
 {'id': 10, 'name': 'Book10', 'publisher_name': 'Publisher1'},
 {'id': 11, 'name': 'Book11', 'publisher_name': 'Publisher1'},
 {'id': 12, 'name': 'Book12', 'publisher_name': 'Publisher1'},
 {'id': 13, 'name': 'Book13', 'publisher_name': 'Publisher1'},
 {'id': 14, 'name': 'Book14', 'publisher_name': 'Publisher1'},
 {'id': 15, 'name': 'Book15', 'publisher_name': 'Publisher1'},
 {'id': 16, 'name': 'Book16', 'publisher_name': 'Publisher1'},
 {'id': 17, 'name': 'Book17', 'publisher_name': 'Publisher1'},
 {'id': 18, 'name': 'Book18', 'publisher_name': 'Publisher1'},
 {'id': 19, 'name': 'Book19', 'publisher_name': 'Publisher1'},
 {'id': 20, 'name': 'Book20', 'publisher_name': 'Publisher1'},
 {'id': 21, 'name': 'Book21', 'publisher_name': 'Publisher2'},
 {'id': 22, 'name': 'Book22', 'publisher_name': 'Publisher2'},
 {'id': 23, 'name': 'Book23', 'publisher_name': 'Publisher2'},
 {'id': 24, 'name': 'Book24', 'publisher_name': 'Publisher2'},
 {'id': 25, 'name': 'Book25', 'publisher_name': 'Publisher2'},
 {'id': 26, 'name': 'Book26', 'publisher_name': 'Publisher2'},
 {'id': 27, 'name': 'Book27', 'publisher_name': 'Publisher2'},
 {'id': 28, 'name': 'Book28', 'publisher_name': 'Publisher2'},
 {'id': 29, 'name': 'Book29', 'publisher_name': 'Publisher2'},
 {'id': 30, 'name': 'Book30', 'publisher_name': 'Publisher2'},
 {'id': 31, 'name': 'Book31', 'publisher_name': 'Publisher2'},
 {'id': 32, 'name': 'Book32', 'publisher_name': 'Publisher2'},
 {'id': 33, 'name': 'Book33', 'publisher_name': 'Publisher2'},
 {'id': 34, 'name': 'Book34', 'publisher_name': 'Publisher2'},
 {'id': 35, 'name': 'Book35', 'publisher_name': 'Publisher2'},
 {'id': 36, 'name': 'Book36', 'publisher_name': 'Publisher2'},
 {'id': 37, 'name': 'Book37', 'publisher_name': 'Publisher2'},
 {'id': 38, 'name': 'Book38', 'publisher_name': 'Publisher2'},
 {'id': 39, 'name': 'Book39', 'publisher_name': 'Publisher2'},
 {'id': 40, 'name': 'Book40', 'publisher_name': 'Publisher2'},
 {'id': 41, 'name': 'Book41', 'publisher_name': 'Publisher3'},
 {'id': 42, 'name': 'Book42', 'publisher_name': 'Publisher3'},
 {'id': 43, 'name': 'Book43', 'publisher_name': 'Publisher3'},
 {'id': 44, 'name': 'Book44', 'publisher_name': 'Publisher3'},
 {'id': 45, 'name': 'Book45', 'publisher_name': 'Publisher3'},
 {'id': 46, 'name': 'Book46', 'publisher_name': 'Publisher3'},
 {'id': 47, 'name': 'Book47', 'publisher_name': 'Publisher3'},
 {'id': 48, 'name': 'Book48', 'publisher_name': 'Publisher3'},
 {'id': 49, 'name': 'Book49', 'publisher_name': 'Publisher3'},
 {'id': 50, 'name': 'Book50', 'publisher_name': 'Publisher3'},
 {'id': 51, 'name': 'Book51', 'publisher_name': 'Publisher3'},
 {'id': 52, 'name': 'Book52', 'publisher_name': 'Publisher3'},
 {'id': 53, 'name': 'Book53', 'publisher_name': 'Publisher3'},
 {'id': 54, 'name': 'Book54', 'publisher_name': 'Publisher3'},
 {'id': 55, 'name': 'Book55', 'publisher_name': 'Publisher3'},
 {'id': 56, 'name': 'Book56', 'publisher_name': 'Publisher3'},
 {'id': 57, 'name': 'Book57', 'publisher_name': 'Publisher3'},
 {'id': 58, 'name': 'Book58', 'publisher_name': 'Publisher3'},
 {'id': 59, 'name': 'Book59', 'publisher_name': 'Publisher3'},
 {'id': 60, 'name': 'Book60', 'publisher_name': 'Publisher3'},
 {'id': 61, 'name': 'Book61', 'publisher_name': 'Publisher4'},
 {'id': 62, 'name': 'Book62', 'publisher_name': 'Publisher4'},
 {'id': 63, 'name': 'Book63', 'publisher_name': 'Publisher4'},
 {'id': 64, 'name': 'Book64', 'publisher_name': 'Publisher4'},
 {'id': 65, 'name': 'Book65', 'publisher_name': 'Publisher4'},
 {'id': 66, 'name': 'Book66', 'publisher_name': 'Publisher4'},
 {'id': 67, 'name': 'Book67', 'publisher_name': 'Publisher4'},
 {'id': 68, 'name': 'Book68', 'publisher_name': 'Publisher4'},
 {'id': 69, 'name': 'Book69', 'publisher_name': 'Publisher4'},
 {'id': 70, 'name': 'Book70', 'publisher_name': 'Publisher4'},
 {'id': 71, 'name': 'Book71', 'publisher_name': 'Publisher4'},
 {'id': 72, 'name': 'Book72', 'publisher_name': 'Publisher4'},
 {'id': 73, 'name': 'Book73', 'publisher_name': 'Publisher4'},
 {'id': 74, 'name': 'Book74', 'publisher_name': 'Publisher4'},
 {'id': 75, 'name': 'Book75', 'publisher_name': 'Publisher4'},
 {'id': 76, 'name': 'Book76', 'publisher_name': 'Publisher4'},
 {'id': 77, 'name': 'Book77', 'publisher_name': 'Publisher4'},
 {'id': 78, 'name': 'Book78', 'publisher_name': 'Publisher4'},
 {'id': 79, 'name': 'Book79', 'publisher_name': 'Publisher4'},
 {'id': 80, 'name': 'Book80', 'publisher_name': 'Publisher4'},
 {'id': 81, 'name': 'Book81', 'publisher_name': 'Publisher5'},
 {'id': 82, 'name': 'Book82', 'publisher_name': 'Publisher5'},
 {'id': 83, 'name': 'Book83', 'publisher_name': 'Publisher5'},
 {'id': 84, 'name': 'Book84', 'publisher_name': 'Publisher5'},
 {'id': 85, 'name': 'Book85', 'publisher_name': 'Publisher5'},
 {'id': 86, 'name': 'Book86', 'publisher_name': 'Publisher5'},
 {'id': 87, 'name': 'Book87', 'publisher_name': 'Publisher5'},
 {'id': 88, 'name': 'Book88', 'publisher_name': 'Publisher5'},
 {'id': 89, 'name': 'Book89', 'publisher_name': 'Publisher5'},
 {'id': 90, 'name': 'Book90', 'publisher_name': 'Publisher5'},
 {'id': 91, 'name': 'Book91', 'publisher_name': 'Publisher5'},
 {'id': 92, 'name': 'Book92', 'publisher_name': 'Publisher5'},
 {'id': 93, 'name': 'Book93', 'publisher_name': 'Publisher5'},
 {'id': 94, 'name': 'Book94', 'publisher_name': 'Publisher5'},
 {'id': 95, 'name': 'Book95', 'publisher_name': 'Publisher5'},
 {'id': 96, 'name': 'Book96', 'publisher_name': 'Publisher5'},
 {'id': 97, 'name': 'Book97', 'publisher_name': 'Publisher5'},
 {'id': 98, 'name': 'Book98', 'publisher_name': 'Publisher5'},
 {'id': 99, 'name': 'Book99', 'publisher_name': 'Publisher5'},
 {'id': 100, 'name': 'Book100', 'publisher_name': 'Publisher5'}]

Function : book_list_select_related
Number of Queries : 1
Finished in : 0.00s

Query (1):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id",
       "django_querys_publisher"."id",
       "django_querys_publisher"."name"
FROM "django_querys_book"
INNER JOIN "django_querys_publisher" ON ("django_querys_book"."publisher_id" = "django_querys_publisher"."id")
"""