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
        self.store_list_expensive_books_prefetch_related()

    @query_debugger
    def store_list_expensive_books_prefetch_related(self):
        queryset = Store.objects.prefetch_related('books')

        stores = []
        for store in queryset:
            books = [book.name for book in store.books.filter(price__range=(250, 300))]
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
$ ./manage.py prefetch_related_filtering_disabled

Stores objects (100):
[
    {'id': 1, 'name': 'Store1', 'books': ['Book2', 'Book3', 'Book11', 'Book13', 'Book27', 'Book40', 'Book46', 'Book51', 'Book59', 'Book64', 'Book68', 'Book72', 'Book78', 'Book81', 'Book88', 'Book95', 'Book97', 'Book98', 'Book100']},
    {'id': 2, 'name': 'Store2', 'books': ['Book2', 'Book3', 'Book11', 'Book13', 'Book27', 'Book40', 'Book46', 'Book51', 'Book59', 'Book64', 'Book68', 'Book72', 'Book78', 'Book81', 'Book88', 'Book95', 'Book97', 'Book98', 'Book100']},
    ...,
    {'id': 100, 'name': 'Store100', 'books': ['Book2', 'Book3', 'Book11', 'Book13', 'Book27', 'Book40', 'Book46', 'Book51', 'Book59', 'Book64', 'Book68', 'Book72', 'Book78', 'Book81', 'Book88', 'Book95', 'Book97', 'Book98', 'Book100']}
]

Function : store_list_expensive_books_prefetch_related
Number of Queries : 102
Finished in : 0.09s

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


Query (3):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 1
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (4):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 2
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (5):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 3
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (6):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 4
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (7):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 5
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (8):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 6
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (9):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 7
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (10):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 8
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (11):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 9
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (12):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 10
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (13):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 11
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (14):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 12
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (15):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 13
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (16):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 14
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (17):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 15
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (18):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 16
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (19):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 17
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (20):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 18
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (21):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 19
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (22):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 20
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (23):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 21
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (24):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 22
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (25):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 23
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (26):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 24
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (27):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 25
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (28):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 26
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (29):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 27
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (30):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 28
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (31):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 29
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (32):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 30
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (33):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 31
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (34):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 32
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (35):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 33
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (36):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 34
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (37):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 35
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (38):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 36
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (39):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 37
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (40):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 38
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (41):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 39
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (42):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 40
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (43):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 41
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (44):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 42
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (45):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 43
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (46):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 44
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (47):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 45
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (48):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 46
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (49):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 47
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (50):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 48
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (51):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 49
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (52):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 50
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (53):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 51
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (54):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 52
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (55):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 53
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (56):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 54
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (57):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 55
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (58):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 56
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (59):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 57
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (60):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 58
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (61):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 59
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (62):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 60
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (63):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 61
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (64):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 62
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (65):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 63
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (66):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 64
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (67):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 65
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (68):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 66
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (69):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 67
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (70):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 68
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (71):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 69
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (72):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 70
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (73):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 71
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (74):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 72
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (75):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 73
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (76):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 74
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (77):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 75
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (78):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 76
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (79):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 77
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (80):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 78
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (81):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 79
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (82):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 80
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (83):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 81
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (84):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 82
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (85):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 83
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (86):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 84
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (87):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 85
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (88):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 86
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (89):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 87
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (90):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 88
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (91):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 89
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (92):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 90
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (93):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 91
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (94):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 92
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (95):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 93
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (96):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 94
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (97):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 95
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (98):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 96
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (99):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 97
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (100):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 98
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (101):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 99
       AND "django_querys_book"."price" BETWEEN 250 AND 300)


Query (102):
SELECT "django_querys_book"."id",
       "django_querys_book"."name",
       "django_querys_book"."price",
       "django_querys_book"."publisher_id"
FROM "django_querys_book"
INNER JOIN "django_querys_store_books" ON ("django_querys_book"."id" = "django_querys_store_books"."book_id")
WHERE ("django_querys_store_books"."store_id" = 100
       AND "django_querys_book"."price" BETWEEN 250 AND 300)
"""