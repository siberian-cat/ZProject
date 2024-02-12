from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class AddressesHome(ListView):
    model = Address
    template_name = 'addresses/index.html'
    context_object_name = 'addrs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список адресов'
        return context


class StreetsHome(ListView):
    model = Street
    template_name = 'addresses/streets/index.html'
    context_object_name = 'strs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список названий улиц'
        return context


class LocalitiesHome(ListView):
    model = Locality
    template_name = 'addresses/localities/index.html'
    context_object_name = 'locs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список населенных пунктов'
        return context


class StreetTypesHome(ListView):
    model = StreetType
    template_name = 'addresses/streets/streettypes/index.html'
    context_object_name = 'strtypes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список типов улиц'
        return context
