from django.db import models

class StreetType(models.Model):
    streettype_name = models.CharField(max_length=255)

