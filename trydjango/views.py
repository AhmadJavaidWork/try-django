import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    random_id = random.randint(1, 4)
    article_obj = Article.objects.get(id=random_id)

    context = {
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content
    }
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)
