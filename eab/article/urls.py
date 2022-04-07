from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViews


router = DefaultRouter()

router.register(r'', ArticleViews, basename="articles")

urlpatterns = [
    path('', include(router.urls))
]
