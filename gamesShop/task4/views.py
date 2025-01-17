from lib2to3.fixes.fix_input import context
#from sys import modules
from django.shortcuts import render
from task1.models import Game

# Create your views here.

def platform_view(request):
    return render(request,'fourth_task/menu.html')

def games_view(request):
    game = list(Game.objects.values_list('title', 'description', 'cost'))

    context = {
        'game': game,
    }
    return render(request,'fourth_task/games.html', context)

def cart_view(request):
    context = {
        'content': 'Извините, выша корзина пуста',
    }
    return render(request,'fourth_task/cart.html', context)