from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def addresses_index(request):
    addrs = Address.objects.all()
    return render(request, 'addresses/index.html', {'title': 'Список адресов', 'addr': addrs})


def localities_index(request):
    return render(request, 'addresses/localities/index.html', {'title':'Список населенных пунктов',
                                                               'header3': 'Здесь будет список населенных пунктов!',
                                                               'header5': 'Ну, потом, когда-нибудь...'})


def streets_index(request):
    return render(request, 'addresses/streets/index.html', {'title':'Список названий улиц',
                                                            'header3': 'Здесь будет список названий улиц!',
                                                            'header5': 'Ну, потом, когда-нибудь...'})


def streettypes_index(request):
    return render(request, 'addresses/streets/streettypes/index.html', {'title':'Список типов улиц',
                                                                        'header3': 'Здесь будет список типов улиц!',
                                                                        'header5': 'Ну, потом, когда-нибудь...'})
