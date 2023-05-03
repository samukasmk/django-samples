from rest_framework import viewsets
from samples.rest_framework_api.models import Article
from samples.rest_framework_api.serializers import ArticleSerializer


class ArticleModelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(self, request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        return super().perform_create(self, serializer)

    def perform_update(self, serializer):
        return super().perform_update(self, serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(self, instance)
