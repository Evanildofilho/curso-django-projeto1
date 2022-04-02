

from django.shortcuts import render

# from urllib.request import Request
# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Evanildo Filho',
    })


""" def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
 """
