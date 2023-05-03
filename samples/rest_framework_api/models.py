from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=110)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}: {self.description}'
