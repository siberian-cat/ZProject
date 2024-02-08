from django.urls import path

from .views import *


urlpatterns = [
    path('', addresses_index, name='addresses'),
    path('localities/', localities_index, name='localities'),
    path('streets/', streets_index, name='streets'),
    path('streets/streettypes', streettypes_index, name='streettypes'),
]