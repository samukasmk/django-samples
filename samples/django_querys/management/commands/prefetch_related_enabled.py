from django.core.management.base import BaseCommand
from samples.django_querys.models import Store
from samples.django_querys.decorators import query_debugger
from pprint import pprint


class Command(BaseCommand):
    """
    This command is for inserting Publisher, Book, Store into database.
    Insert 5 Publishers, 100 Books, 10 Stores.
    """

    def handle(self, *args, **options):
        self.store_list_prefetch_related()

    @query_debugger
    def store_list_prefetch_related(self):
        queryset = Store.objects.prefetch_related('books')

        stores = []

        for store in queryset:
            books = [book.name for book in store.books.all()]
            stores.append({'id': store.id, 'name': store.name,
                           'books': books})

        self.print_stores_objects(stores)
        return stores

    def print_stores_objects(self, stores):
        print(f'\nStores objects ({len(stores)}):')
        print('[')
        print(f'    {stores[0]},')
        print(f'    {stores[1]},')
        print('    ...,')
        print(f'    {stores[99]}')
        print(']\n')

"""
$ ./manage.py prefetch_related_enabled

Stores objects (100):
[
    {'id': 1, 'name': 'Store1', 'books': ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6', 'Book7', 'Book8', 'Book9', 'Book10', 'Book11', 'Book12', 'Book13', 'Book14', 'Book15', 'Book16', 'Book17', 'Book18', 'Book19', 'Book20', 'Book21', 'Book22', 'Book23', 'Book24', 'Book25', 'Book26', 'Book27', 'Book28', 'Book29', 'Book30', 'Book31', 'Book32', 'Book33', 'Book34', 'Book35', 'Book36', 'Book37', 'Book38', 'Book39', 'Book40', 'Book41', 'Book42', 'Book43', 'Book44', 'Book45', 'Book46', 'Book47', 'Book48', 'Book49', 'Book50', 'Book51', 'Book52', 'Book53', 'Book54', 'Book55', 'Book56', 'Book57', 'Book58', 'Book59', 'Book60', 'Book61', 'Book62', 'Book63', 'Book64', 'Book65', 'Book66', 'Book67', 'Book68', 'Book69', 'Book70', 'Book71', 'Book72', 'Book73', 'Book74', 'Book75', 'Book76', 'Book77', 'Book78', 'Book79', 'Book80', 'Book81', 'Book82', 'Book83', 'Book84', 'Book85', 'Book86', 'Book87', 'Book88', 'Book89', 'Book90', 'Book91', 'Book92', 'Book93', 'Book94', 'Book95', 'Book96', 'Book97', 'Book98', 'Book99', 'Book100']},
    {'id': 2, 'name': 'Store2', 'books': ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6', 'Book7', 'Book8', 'Book9', 'Book10', 'Book11', 'Book12', 'Book13', 'Book14', 'Book15', 'Book16', 'Book17', 'Book18', 'Book19', 'Book20', 'Book21', 'Book22', 'Book23', 'Book24', 'Book25', 'Book26', 'Book27', 'Book28', 'Book29', 'Book30', 'Book31', 'Book32', 'Book33', 'Book34', 'Book35', 'Book36', 'Book37', 'Book38', 'Book39', 'Book40', 'Book41', 'Book42', 'Book43', 'Book44', 'Book45', 'Book46', 'Book47', 'Book48', 'Book49', 'Book50', 'Book51', 'Book52', 'Book53', 'Book54', 'Book55', 'Book56', 'Book57', 'Book58', 'Book59', 'Book60', 'Book61', 'Book62', 'Book63', 'Book64', 'Book65', 'Book66', 'Book67', 'Book68', 'Book69', 'Book70', 'Book71', 'Book72', 'Book73', 'Book74', 'Book75', 'Book76', 'Book77', 'Book78', 'Book79', 'Book80', 'Book81', 'Book82', 'Book83', 'Book84', 'Book85', 'Book86', 'Book87', 'Book88', 'Book89', 'Book90', 'Book91', 'Book92', 'Book93', 'Book94', 'Book95', 'Book96', 'Book97', 'Book98', 'Book99', 'Book100']},
    ...,
    {'id': 100, 'name': 'Store100', 'books': ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6', 'Book7', 'Book8', 'Book9', 'Book10', 'Book11', 'Book12', 'Book13', 'Book14', 'Book15', 'Book16', 'Book17', 'Book18', 'Book19', 'Book20', 'Book21', 'Book22', 'Book23', 'Book24', 'Book25', 'Book26', 'Book27', 'Book28', 'Book29', 'Book30', 'Book31', 'Book32', 'Book33', 'Book34', 'Book35', 'Book36', 'Book37', 'Book38', 'Book39', 'Book40', 'Book41', 'Book42', 'Book43', 'Book44', 'Book45', 'Book46', 'Book47', 'Book48', 'Book49', 'Book50', 'Book51', 'Book52', 'Book53', 'Book54', 'Book55', 'Book56', 'Book57', 'Book58', 'Book59', 'Book60', 'Book61', 'Book62', 'Book63', 'Book64', 'Book65', 'Book66', 'Book67', 'Book68', 'Book69', 'Book70', 'Book71', 'Book72', 'Book73', 'Book74', 'Book75', 'Book76', 'Book77', 'Book78', 'Book79', 'Book80', 'Book81', 'Book82', 'Book83', 'Book84', 'Book85', 'Book86', 'Book87', 'Book88', 'Book89', 'Book90', 'Book91', 'Book92', 'Book93', 'Book94', 'Book95', 'Book96', 'Book97', 'Book98', 'Book99', 'Book100']}
]

Function : store_list_prefetch_related
Number of Queries : 2
Finished in : 0.05s

Query (1):
SELECT "django_querys_store"."id",
       "django_querys_store"."name"
FROM "django_querys_store"


Query (2):
SELECT ("django_querys_store_books"."store_id") AS "_prefetch_related_val_store_id",
       "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" IN (1,
                                                 2,
                                                 3,
                                                 4,
                                                 5,
                                                 6,
                                                 7,
                                                 8,
                                                 9,
                                                 10,
                                                 11,
                                                 12,
                                                 13,
                                                 14,
                                                 15,
                                                 16,
                                                 17,
                                                 18,
                                                 19,
                                                 20,
                                                 21,
                                                 22,
                                                 23,
                                                 24,
                                                 25,
                                                 26,
                                                 27,
                                                 28,
                                                 29,
                                                 30,
                                                 31,
                                                 32,
                                                 33,
                                                 34,
                                                 35,
                                                 36,
                                                 37,
                                                 38,
                                                 39,
                                                 40,
                                                 41,
                                                 42,
                                                 43,
                                                 44,
                                                 45,
                                                 46,
                                                 47,
                                                 48,
                                                 49,
                                                 50,
                                                 51,
                                                 52,
                                                 53,
                                                 54,
                                                 55,
                                                 56,
                                                 57,
                                                 58,
                                                 59,
                                                 60,
                                                 61,
                                                 62,
                                                 63,
                                                 64,
                                                 65,
                                                 66,
                                                 67,
                                                 68,
                                                 69,
                                                 70,
                                                 71,
                                                 72,
                                                 73,
                                                 74,
                                                 75,
                                                 76,
                                                 77,
                                                 78,
                                                 79,
                                                 80,
                                                 81,
                                                 82,
                                                 83,
                                                 84,
                                                 85,
                                                 86,
                                                 87,
                                                 88,
                                                 89,
                                                 90,
                                                 91,
                                                 92,
                                                 93,
                                                 94,
                                                 95,
                                                 96,
                                                 97,
                                                 98,
                                                 99,
                                                 100)
"""