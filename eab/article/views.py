from django.shortcuts import render
from rest_framework import viewsets

from article.serializers import ArticleSerializer
from .models import Article

# Create your views here.


class ArticleViews(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
