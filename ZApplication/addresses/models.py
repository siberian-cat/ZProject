from django.db import models


class StreetType(models.Model):
    streettype_name = models.CharField(max_length=50)


class Street(models.Model):
    street_name = models.CharField(max_length=255)
    streettype = models.ForeignKey(StreetType, related_name="streettypes", on_delete=models.PROTECT)


class Locality(models.Model):
    locality_name = models.CharField(max_length=100)


class Address(models.Model):
    build_num = models.CharField(max_length=50)
    locality = models.ForeignKey(Locality, related_name="localities", on_delete=models.PROTECT)
    street = models.ForeignKey(Street, related_name="streets", on_delete=models.PROTECT)

