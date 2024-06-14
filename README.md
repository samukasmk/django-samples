# django-samples
It's sample peaces of code in Django to easily remembers.



## Advanced Django Querys

### Select related samples:
- [select_related_disable.py](samples/django_querys/management/commands/select_related_disable.py) with 101 querys for each object
- [select_related_enabled.py](samples/django_querys/management/commands/select_related_enabled.py) reduced for 1 query in inner join
- [select_related_enabled_defer.py](samples/django_querys/management/commands/select_related_enabled_defer.py) without a specific field

### Prefetch related samples:
- [prefetch_related_disabled.py](samples/django_querys/management/commands/prefetch_related_disabled.py) with 101 querys for each object
- [prefetch_related_enabled.py](samples/django_querys/management/commands/prefetch_related_enabled.py) reduced for 2 querys in inner join

### Prefetch related samples in cross references:
- [prefetch_related_filtering_disabled.py](samples/django_querys/management/commands/prefetch_related_filtering_disabled.py) with 102 querys for each sub object
- [prefetch_related_filtering_enabled.py](samples/django_querys/management/commands/prefetch_related_filtering_enabled.py) reduced for 2 querys in inner join

