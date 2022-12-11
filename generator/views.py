import random

from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'fronten/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuwvxyz')

    if request.GET.get('upercase'):
        characters.extend(list('ABCDEFGHIJKLMNNQRSTUVWXYZ'))

        if request.GET.get('numbers'):
            characters.extend(list('0123456789'))

        if request.GET.get('special'):
            characters.extend(list('!@#$%^&*(){}[]|><?/~'))

    lenght =  int(request.GET.get('length'))
    therepassword = ''

    for x in range(lenght):
        therepassword += random.choice(characters)

    return render(request, 'fronten/password.html', {'password': therepassword})
