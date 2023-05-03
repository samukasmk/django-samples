# Django Rest Framework: Shortcuts

## APIView

### Function-based APIView
> a Django Function-based View with a decorator

https://www.django-rest-framework.org/api-guide/views/#function-based-views

```python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(http_method_names=['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message":"Welcome Home!"},
                    status=status.HTTP_200_OK)

```

### Class-based APIView
> a extesion from Django Class-based View

https://www.django-rest-framework.org/api-guide/views/#class-based-views

views.py
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

```


### Sample Model Endpoint Views
https://medium.com/@arrosid/introduction-to-genericapiview-in-django-rest-framework-eb557bf986b2

views.py
```python
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers

class ArticleListCreateAPIView(APIView):
    def get(self, request):
        articles = models.Article.objects.all()
        serializer = serializers.ArticleSerializer(articles,   
                                                  many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=serializers.ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                           status=status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                       status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):
    def get(self, request, pk):
        article = models.Article.objects.get(id=pk)
        serializer = serializers.ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = models.Article.objects.get(id=pk)
        serializer = serializers.ArticleSerializer(article, 
                                                  request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = models.Article.objects.get(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.home),
               path('article/', views.ArticleListCreateView.as_view()),
               path('article/<int:pk>/', views.ArticleDetailView.as_view())]
```




## GenericAPIView class
> GenericAPIView extends APIView class

> The porpusoe is adding commonly required behavior for standard list and detail views like model object managament, paginating, filtering

https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview

GenericAPIView defines ready-to-use attributes like:
- queryset
- serializer_class
- lookup_field
- lookup_url_kwarg
- filter_backends
- pagination_class

And ready-to-use method like:
- get_queryset
- get_object
- get_serializer
- get_serializer_class
- filter_queryset
- paginate_queryset
- get_paginated_response


## Concrete View Classes
> Concrete View Classes extends GenericAPIView class

Concrete View Classes were created to define REST API methods like:
- get
- post
- put
- patch
- delete

Although without the need to define them because already defined in the classes:
- CreateAPIView
- ListAPIView
- RetrieveAPIView
- DestroyAPIView
- UpdateAPIView
- ListCreateAPIView
- RetrieveUpdateAPIView
- RetrieveDestroyAPIView
- RetrieveUpdateDestroyAPIView


### Using concrete view classes

https://medium.com/@arrosid/introduction-to-genericapiview-in-django-rest-framework-eb557bf986b2

views.py
```python
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
```

urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.home),
               path('article/', views.ArticleListCreateView.as_view()),
               path('article/<int:pk>/', views.ArticleDetailView.as_view())]
```

### Rewriting GenericAPIView with builtin mixins

https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py

views.py
```python
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


class ArticleListCreateAPIView(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               GenericAPIView):
    """
    Rewriting builtin ListCreateAPIView concrete view for listing a queryset or creating a model instance.
    """
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleDetailRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):
    """
    Rewriting builtin RetrieveUpdateDestroyAPIView concrete view for retrieving,
    updating or deleting a model instance.
    """
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
                                       

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

```

urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.home),
               path('article/', views.ArticleListCreateAPIView.as_view()),
               path('article/<int:pk>/', views.ArticleDetailRetrieveUpdateDestroyAPIView.as_view())]
```



## Rewriting builtin mixins (deeper customization in builtin mixins)
https://github.com/encode/django-rest-framework/blob/master/rest_framework/mixins.py











































## APIException (Customizing exceptions)
> The base class for all exceptions raised inside an APIView class or @api_view

https://www.django-rest-framework.org/api-guide/views/#class-based-views

exceptions.py
```python
from rest_framework.exceptions import APIException

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'
```

views.py
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from excpetions import ServiceUnavailable

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        try:
            usernames = [user.username for user in User.objects.all()]
            return Response(usernames)
        except Exception as exc:
            raise ServiceUnavailable() from exc
```
