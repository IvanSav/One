from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, RequestContext, render, redirect
from oneapp.models import Article
from forms import OrderForm
from time import time
from datetime import date, time, datetime
from django.core.context_processors import csrf
# Create your views here.

def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})

def article(request, article_id=1):
    order_form = OrderForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['form'] = order_form
    return render_to_response('article.html', args)  


def example(request, article_id):
    args = {}
    args['article'] = Article.objects.get(id=article_id)
    return render_to_response('example.html', args)

def addorder(request, article_id):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_title=str(datetime.now())
            order.order_article=Article.objects.get(id=article_id)
            form.save()
    return redirect('articles/get/%s/' % article_id)