#from django.http import HttpRequest
from lib2to3.fixes.fix_input import context
from sys import modules

from django.http import HttpResponse
from django.shortcuts import render
from task1.models import Buyer

from .forms import UserRegister






# Create your views here.


def sign_up_by_html(request):
    users = list(Buyer.objects.all().values_list("name", flat=True))
    info = {}
    if request.method == 'POST':
        # Получаем данные из формы:
        info['username'] = request.POST.get('username')
        info['password'] = request.POST.get('password')
        info['repeat_password'] = request.POST.get('repeat_password')
        age = request.POST.get('age')
        info['age'] = int(age)

        context = form_validation(request, users, info)
        return render(request, 'fifth_task/registration_page.html', context)

    else:
        return render(request, 'fifth_task/registration_page.html')

def sign_up_by_django(request):
    users = list(Buyer.objects.all().values_list("name", flat=True))
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
           info['username'] = form.cleaned_data['username']
           info['password'] = form.cleaned_data['password']
           info['repeat_password'] = form.cleaned_data['repeat_password']
           info['age'] = form.cleaned_data['age']

           context = form_validation(request, users, info)
           return render(request, 'fifth_task/registration_page.html', context)



        else:
            return render(request, 'fifth_task/registration_page.html')

    else:
        form = UserRegister()
    return render(request,'fifth_task/registration_page.html', {'form': form})


def form_validation(request, arg, kwarg):
    users = arg
    info = kwarg
    context = {
        'info': info,
        'form': UserRegister(),
        'error': '',
        'text': '',
    }
    if info['password'] == info['repeat_password'] and info['age'] >= 18 and info['username'] not in users:
        #print(f'users_222: {users}, {info["username"]}, {info["age"]}')
        Buyer.objects.create(name=info['username'], balance=0, age=info['age'])
        context['text'] = f'Приветствуем, {info['username']}!'
        return  context
    elif info['password'] != info['repeat_password']:
        context['error'] = 'Пароли не совпадают'
        return  context
    elif info['age'] < 18:
        context['error'] = 'Вы должны быть старше 18 лет'
        return  context
    elif info['username'] in users:
        context['error'] = 'Пользователь уже существует'
        return  context

