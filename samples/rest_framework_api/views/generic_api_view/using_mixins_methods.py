from rest_framework import generics, mixins
from samples.rest_framework_api.models import Article
from samples.rest_framework_api.serializers import ArticleSerializer


class ArticleListCreateAPIView(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               generics.GenericAPIView):
    """
    Rewriting builtin ListCreateAPIView concrete view for listing a queryset or creating a model instance.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleDetailRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                                mixins.UpdateModelMixin,
                                                mixins.DestroyModelMixin,
                                                generics.GenericAPIView):
    """
    Rewriting builtin RetrieveUpdateDestroyAPIView concrete view for retrieving,
    updating or deleting a model instance.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
