import django_tables2 as tables
from .models import *

class StreetTypesTable(tables.Table):
    class Meta:
        model = StreetType
        # template_name = "django_tables2/bootstrap.html"
        fields = ("streettype_name", )