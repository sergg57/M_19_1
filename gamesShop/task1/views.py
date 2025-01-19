from lib2to3.fixes.fix_input import context

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News

def news(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})

# Create your views here.
