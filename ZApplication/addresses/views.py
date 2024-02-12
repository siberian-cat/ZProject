from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class AddressesHome(ListView):
    model = Address
    template_name = 'addresses/index.html'
    context_object_name = 'addrs'
    extra_context = {'title': 'Список адресов'}


class StreetsHome(ListView):
    model = Street
    template_name = 'addresses/streets/index.html'
    context_object_name = 'strs'
    extra_context = {'title': 'Список названий улиц'}


class LocalitiesHome(ListView):
    model = Locality
    template_name = 'addresses/localities/index.html'
    context_object_name = 'locs'
    extra_context = {'title': 'Список населенных пунктов'}


class StreetTypesHome(ListView):
    model = StreetType
    template_name = 'addresses/streets/streettypes/index.html'
    context_object_name = 'strtypes'
    extra_context = {'title': 'Список типов улиц'}
