from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

'''from . import models
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles':articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return  render(request, '', {'article':article})


def edit_page(request):
    return  render(request, 'edit_page.html')
'''