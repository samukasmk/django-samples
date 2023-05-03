from rest_framework import generics
from samples.rest_framework_api.models import Article
from samples.rest_framework_api.serializers import ArticleSerializer


class PurchaseList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """

        username = self.request.query_params.get('username')
        if username is not None:
            queryset = self.queryset.filter(purchaser__username=username)
        return queryset