from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from samples.rest_framework_api.models import Article
from rest_framework.exceptions import APIException


class ArticleListCreateAPIView(APIView):
    """
    View to list all Articles in the database.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        articles = [{"id": article.pk,
                     "title": article.title,
                     "description": article.description}
                    for article in Article.objects.all()]
        return Response(articles, status=status.HTTP_200_OK)

    def post(self, request):
        if "title" not in request.data or "description" not in request.data:
            raise APIException("Missing json fields: 'title', 'description'")
        created_article = Article.objects.create(title=request.data["title"],
                                                 description=request.data["description"])
        return Response({"id": created_article.pk,
                         "title": created_article.title,
                         "description": created_article.description},
                        status=status.HTTP_201_CREATED)


class ArticleDetailAPIView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        return Response({"id": article.pk,
                         "title": article.title,
                         "description": article.description},
                        status=status.HTTP_200_OK)

    def put(self, request, pk):
        articles = Article.objects.filter(pk=pk)
        articles.update(**request.data)
        article = articles.first()
        return Response({"id": article.pk,
                         "title": article.title,
                         "description": article.description},
                        status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Article.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
