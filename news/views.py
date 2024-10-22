

from django.shortcuts import render
from .models import News_post

def news_list(request):
    news = News_post.objects.select_related('author').all()
    return render(request, 'news/news.html', {'news': news})


