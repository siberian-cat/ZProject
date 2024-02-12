from django.urls import path

from .views import *


urlpatterns = [
    path('', AddressesHome.as_view(), name='addresses'),
    path('localities/', LocalitiesHome.as_view(), name='localities'),
    path('streets/', StreetsHome.as_view(), name='streets'),
    path('streets/streettypes', StreetTypesHome.as_view(), name='streettypes'),
]