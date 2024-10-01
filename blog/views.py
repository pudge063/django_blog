from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.filter(date__lte=timezone.now()).order_by('-date')
    
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, "blog/index.html", {'articles': articles, 'form': form})
