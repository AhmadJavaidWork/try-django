import random
from django.http import HttpResponse


def home_view(request):
    name = "Justin"
    number = random.randint(10, 12938742)
    HTML_STRING = f"""
    <h1>Hello {name} - {number}</h1>
    """
    return HttpResponse(HTML_STRING)
