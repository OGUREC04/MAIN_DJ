from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Article, Comment

def index_second(request):
    latest_article = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_article': latest_article})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('NO1')

    latest_com = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html',{'article':a, 'latest_com': latest_com})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('NO1')

    a.comment_set.create(name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('articles:detail', args=str(a.id)) )