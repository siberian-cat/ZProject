import psycopg2
from django.db import models


class StreetType(models.Model):
    streettype_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.streettype_name}"


class Street(models.Model):
    street_name = models.CharField(max_length=255)
    streettype = models.ForeignKey(StreetType, related_name="streets", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.street_name} {self.streettype.streettype_name}"


class Locality(models.Model):
    locality_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.locality_name}"


class Address(models.Model):
    build_num = models.CharField(max_length=50)
    locality = models.ForeignKey(Locality, related_name="addresses", on_delete=models.PROTECT)
    street = models.ForeignKey(Street, related_name="addresses", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.locality.locality_name}, {self.street.street_name} {self.street.streettype.streettype_name}, {self.build_num}"
