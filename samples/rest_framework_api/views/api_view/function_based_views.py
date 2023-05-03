from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from samples.rest_framework_api.models import Article


@api_view(http_method_names=['GET', 'POST'])
def article_list_create_apiview(request):
    if request.method == 'GET':
        articles = [{"id": article.pk,
                     "title": article.title,
                     "description": article.description}
                    for article in Article.objects.all()]
        return Response(articles, status=status.HTTP_200_OK)

    if request.method == 'POST':
        if "title" not in request.data or "description" not in request.data:
            raise APIException("Missing json fields: 'title', 'description'")
        created_article = Article.objects.create(title=request.data["title"],
                                                 description=request.data["description"])
        return Response({"id": created_article.pk,
                         "title": created_article.title,
                         "description": created_article.description},
                        status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def article_detail_apiview(request, pk):
    if request.method == 'GET':
        article = Article.objects.get(pk=pk)
        return Response({"id": article.pk,
                         "title": article.title,
                         "description": article.description},
                        status=status.HTTP_200_OK)

    if request.method == 'PUT':
        articles = Article.objects.filter(pk=pk)
        articles.update(**request.data)
        article = articles.first()
        return Response({"id": article.pk,
                         "title": article.title,
                         "description": article.description},
                        status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        Article.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
