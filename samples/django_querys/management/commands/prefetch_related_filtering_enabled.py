from django.core.management.base import BaseCommand
from django.db.models import Prefetch
from samples.django_querys.models import Store, Book
from samples.django_querys.decorators import query_debugger
from pprint import pprint


class Command(BaseCommand):
    """
    This command is for inserting Publisher, Book, Store into database.
    Insert 5 Publishers, 100 Books, 10 Stores.
    """

    def handle(self, *args, **options):
        self.store_list_expensive_books_prefetch_related_efficient()

    @query_debugger
    def store_list_expensive_books_prefetch_related_efficient(self):

        queryset = Store.objects.prefetch_related(
            Prefetch('books', queryset=Book.objects.filter(price__range=(250, 300))))

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
./manage.py prefetch_related_filtering_enabled

Stores objects (100):
[
    {'id': 1, 'name': 'Store1', 'books': ['Book2', 'Book3', 'Book11', 'Book13', 'Book27', 'Book40', 'Book46', 'Book51', 'Book59', 'Book64', 'Book68', 'Book72', 'Book78', 'Book81', 'Book88', 'Book95', 'Book97', 'Book98', 'Book100']},
    {'id': 2, 'name': 'Store2', 'books': ['Book2', 'Book3', 'Book11', 'Book13', 'Book27', 'Book40', 'Book46', 'Book51', 'Book59', 'Book64', 'Book68', 'Book72', 'Book78', 'Book81', 'Book88', 'Book95', 'Book97', 'Book98', 'Book100']},
    ...,
    {'id': 100, 'name': 'Store100', 'books': ['Book2', 'Book3', 'Book11', 'Book13', 'Book27', 'Book40', 'Book46', 'Book51', 'Book59', 'Book64', 'Book68', 'Book72', 'Book78', 'Book81', 'Book88', 'Book95', 'Book97', 'Book98', 'Book100']}
]

Function : store_list_expensive_books_prefetch_related_efficient
Number of Queries : 2
Finished in : 0.01s

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
WHERE ("django_querys_book"."price" BETWEEN 250 AND 300
       AND "django_querys_store_books"."store_id" IN (1,
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
                                                      100))
"""