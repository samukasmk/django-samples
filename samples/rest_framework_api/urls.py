from django.urls import path, include
from rest_framework.routers import DefaultRouter

from samples.rest_framework_api.views.api_view import function_based_views, class_based_views, serializer_crud
from samples.rest_framework_api.views.generic_api_view import concrete_view_classes, using_mixins_methods
from samples.rest_framework_api.views.model_viewsets import bultin_model_viewset

router = DefaultRouter()
router.register(r'articles', bultin_model_viewset.ArticleModelViewSet, basename="article")

urlpatterns = [
    # samples of function views
    path('rest_framework/api_view/function/articles/', function_based_views.article_list_create_apiview),
    path('rest_framework/api_view/function/articles/<int:pk>/', function_based_views.article_detail_apiview),

    # samples of simple class views
    path('rest_framework/api_view/class/articles/', class_based_views.ArticleListCreateAPIView.as_view()),
    path('rest_framework/api_view/class/articles/<int:pk>/', class_based_views.ArticleDetailAPIView.as_view()),

    # samples of serializer crud views
    path('rest_framework/api_view/serializer_crud/articles/', serializer_crud.ArticleListCreateAPIView.as_view()),
    path('rest_framework/api_view/serializer_crud/articles/<int:pk>/', serializer_crud.ArticleDetailAPIView.as_view()),

    # samples of generic api view: with concrete view classes
    path('rest_framework/generic_api_view/concrete_view_classes/articles/',
         concrete_view_classes.ArticleListCreateView.as_view()),
    path('rest_framework/generic_api_view/concrete_view_classes/articles/<int:pk>/',
         concrete_view_classes.ArticleDetailView.as_view()),

    # samples of generic api view: rewriting the mixins classes
    # path('rest_framework/generic_api_view/rewriting_mixins/article/', rewriting_mixins.ArticleListCreateView.as_view()),
    # path('rest_framework/generic_api_view/rewriting_mixins/article/<int:pk>/',
    #      rewriting_mixins.ArticleDetailView.as_view()),

    path('', include(router.urls)),

]
