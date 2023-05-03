import time
import functools

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format
from django.db import connection, reset_queries


def print_sql(query_object, number):
    formatted = format(query_object['sql'], reindent=True)
    print(f'\nQuery ({number}):')
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))


def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")

        for index, query in enumerate(connection.queries):
            print_sql(query, index + 1)
        return result

    return inner_func
