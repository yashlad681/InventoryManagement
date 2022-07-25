import random
from django.http import HttpResponse

from django.template.loader import render_to_string
from articles.models import Article



def home_view(request, id=None, *args, **kwargs):
    """
    Take in request,django sends response
    """

    random_id = random.randint(1, 2)
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()

    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }
    HTML_STRING = render_to_string("home-view.html", context=context)
    # article_obj = Article.obj.get(id=pk)
    # article_title = article_obj.title
    # article_content = article_obj.content
    return HttpResponse(HTML_STRING)
