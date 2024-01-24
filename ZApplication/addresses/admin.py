from django.contrib import admin

from addresses.models import StreetType, Street, Locality, Address

admin.site.register(StreetType)
admin.site.register(Street)
admin.site.register(Locality)
admin.site.register(Address)
