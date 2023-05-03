from rest_framework import viewsets
from samples.rest_framework_api.models import Article
from samples.rest_framework_api.serializers import ArticleSerializer

class ArticleModelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer