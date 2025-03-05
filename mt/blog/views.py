from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer

@api_view(["GET"])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def article_detail(request, id):
    article = Article.objects.get(id=id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
