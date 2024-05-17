import random
from django.http import HttpResponse

from articles.models import Article


def home_view(request):
    random_id = random.randint(1, 4)
    article_obj = Article.objects.get(id=random_id)
    H1_STRING = f"""
    <h1>{article_obj.title} ({article_obj.id})!</h1>
    """
    P1_STRING = f"""
    <p>{article_obj.content}!</p>
    """
    HTML_STRING = H1_STRING + P1_STRING
    return HttpResponse(HTML_STRING)
