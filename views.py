from django.shortcuts import render
from news.models import newsItem

def news_index(request):
    context = {
        'news': newsItem.objects.all()
    }
    return render(request, 'news_index.html', context)

