from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

def create(request):
    rep = Reporter(first_name='Guillermo', last_name='Dulce', email="guille@demo.com")
    rep.save()

    art1 = Article(headline='Lorem ipsum dolot', pub_date=date(2022,5,5), reporter=rep)
    art1.save()
    art2 = Article(headline='Sarasa titulo', pub_date=date(2022,3,7), reporter=rep)
    art2.save()
    art3 = Article(headline='Este es el headline', pub_date=date(2022,4,9), reporter=rep)
    art3.save()

    result = rep.article_set.count()
    # result = rep.article_set.filter(headline='Este es el headline')
    # result = art1.reporter.first_name

    return HttpResponse(result)