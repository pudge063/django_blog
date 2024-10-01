from django.utils import timezone
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.filter(date__lte=timezone.now()).order_by('date')

    return render(request, "blog/index.html", {'articles': articles})


# def publish(request):

#     return render(request, "blog/index.html")