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
        self.store_list()

    @query_debugger
    def store_list(self):
        queryset = Store.objects.all()

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
$ ./manage.py prefetch_related_disabled

Stores objects (100):
[
    {'id': 1, 'name': 'Store1', 'books': ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6', 'Book7', 'Book8', 'Book9', 'Book10', 'Book11', 'Book12', 'Book13', 'Book14', 'Book15', 'Book16', 'Book17', 'Book18', 'Book19', 'Book20', 'Book21', 'Book22', 'Book23', 'Book24', 'Book25', 'Book26', 'Book27', 'Book28', 'Book29', 'Book30', 'Book31', 'Book32', 'Book33', 'Book34', 'Book35', 'Book36', 'Book37', 'Book38', 'Book39', 'Book40', 'Book41', 'Book42', 'Book43', 'Book44', 'Book45', 'Book46', 'Book47', 'Book48', 'Book49', 'Book50', 'Book51', 'Book52', 'Book53', 'Book54', 'Book55', 'Book56', 'Book57', 'Book58', 'Book59', 'Book60', 'Book61', 'Book62', 'Book63', 'Book64', 'Book65', 'Book66', 'Book67', 'Book68', 'Book69', 'Book70', 'Book71', 'Book72', 'Book73', 'Book74', 'Book75', 'Book76', 'Book77', 'Book78', 'Book79', 'Book80', 'Book81', 'Book82', 'Book83', 'Book84', 'Book85', 'Book86', 'Book87', 'Book88', 'Book89', 'Book90', 'Book91', 'Book92', 'Book93', 'Book94', 'Book95', 'Book96', 'Book97', 'Book98', 'Book99', 'Book100']},
    {'id': 2, 'name': 'Store2', 'books': ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6', 'Book7', 'Book8', 'Book9', 'Book10', 'Book11', 'Book12', 'Book13', 'Book14', 'Book15', 'Book16', 'Book17', 'Book18', 'Book19', 'Book20', 'Book21', 'Book22', 'Book23', 'Book24', 'Book25', 'Book26', 'Book27', 'Book28', 'Book29', 'Book30', 'Book31', 'Book32', 'Book33', 'Book34', 'Book35', 'Book36', 'Book37', 'Book38', 'Book39', 'Book40', 'Book41', 'Book42', 'Book43', 'Book44', 'Book45', 'Book46', 'Book47', 'Book48', 'Book49', 'Book50', 'Book51', 'Book52', 'Book53', 'Book54', 'Book55', 'Book56', 'Book57', 'Book58', 'Book59', 'Book60', 'Book61', 'Book62', 'Book63', 'Book64', 'Book65', 'Book66', 'Book67', 'Book68', 'Book69', 'Book70', 'Book71', 'Book72', 'Book73', 'Book74', 'Book75', 'Book76', 'Book77', 'Book78', 'Book79', 'Book80', 'Book81', 'Book82', 'Book83', 'Book84', 'Book85', 'Book86', 'Book87', 'Book88', 'Book89', 'Book90', 'Book91', 'Book92', 'Book93', 'Book94', 'Book95', 'Book96', 'Book97', 'Book98', 'Book99', 'Book100']},
    ...,
    {'id': 100, 'name': 'Store100', 'books': ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6', 'Book7', 'Book8', 'Book9', 'Book10', 'Book11', 'Book12', 'Book13', 'Book14', 'Book15', 'Book16', 'Book17', 'Book18', 'Book19', 'Book20', 'Book21', 'Book22', 'Book23', 'Book24', 'Book25', 'Book26', 'Book27', 'Book28', 'Book29', 'Book30', 'Book31', 'Book32', 'Book33', 'Book34', 'Book35', 'Book36', 'Book37', 'Book38', 'Book39', 'Book40', 'Book41', 'Book42', 'Book43', 'Book44', 'Book45', 'Book46', 'Book47', 'Book48', 'Book49', 'Book50', 'Book51', 'Book52', 'Book53', 'Book54', 'Book55', 'Book56', 'Book57', 'Book58', 'Book59', 'Book60', 'Book61', 'Book62', 'Book63', 'Book64', 'Book65', 'Book66', 'Book67', 'Book68', 'Book69', 'Book70', 'Book71', 'Book72', 'Book73', 'Book74', 'Book75', 'Book76', 'Book77', 'Book78', 'Book79', 'Book80', 'Book81', 'Book82', 'Book83', 'Book84', 'Book85', 'Book86', 'Book87', 'Book88', 'Book89', 'Book90', 'Book91', 'Book92', 'Book93', 'Book94', 'Book95', 'Book96', 'Book97', 'Book98', 'Book99', 'Book100']}
]

Function : store_list
Number of Queries : 101
Finished in : 0.05s

Query (1):
SELECT "django_querys_store"."id",
       "django_querys_store"."name"
FROM "django_querys_store"


Query (2):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 1


Query (3):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 2


Query (4):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 3


Query (5):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 4


Query (6):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 5


Query (7):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 6


Query (8):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 7


Query (9):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 8


Query (10):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 9


Query (11):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 10


Query (12):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 11


Query (13):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 12


Query (14):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 13


Query (15):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 14


Query (16):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 15


Query (17):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 16


Query (18):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 17


Query (19):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 18


Query (20):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 19


Query (21):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 20


Query (22):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 21


Query (23):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 22


Query (24):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 23


Query (25):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 24


Query (26):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 25


Query (27):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 26


Query (28):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 27


Query (29):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 28


Query (30):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 29


Query (31):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 30


Query (32):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 31


Query (33):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 32


Query (34):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 33


Query (35):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 34


Query (36):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 35


Query (37):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 36


Query (38):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 37


Query (39):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 38


Query (40):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 39


Query (41):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 40


Query (42):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 41


Query (43):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 42


Query (44):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 43


Query (45):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 44


Query (46):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 45


Query (47):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 46


Query (48):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 47


Query (49):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 48


Query (50):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 49


Query (51):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 50


Query (52):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 51


Query (53):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 52


Query (54):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 53


Query (55):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 54


Query (56):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 55


Query (57):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 56


Query (58):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 57


Query (59):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 58


Query (60):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 59


Query (61):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 60


Query (62):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 61


Query (63):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 62


Query (64):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 63


Query (65):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 64


Query (66):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 65


Query (67):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 66


Query (68):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 67


Query (69):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 68


Query (70):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 69


Query (71):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 70


Query (72):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 71


Query (73):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 72


Query (74):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 73


Query (75):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 74


Query (76):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 75


Query (77):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 76


Query (78):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 77


Query (79):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 78


Query (80):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 79


Query (81):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 80


Query (82):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 81


Query (83):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 82


Query (84):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 83


Query (85):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 84


Query (86):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 85


Query (87):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 86


Query (88):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 87


Query (89):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 88


Query (90):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 89


Query (91):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 90


Query (92):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 91


Query (93):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 92


Query (94):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 93


Query (95):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 94


Query (96):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 95


Query (97):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 96


Query (98):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 97


Query (99):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 98


Query (100):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 99


Query (101):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE "django_querys_store_books"."store_id" = 100
"""