from django.db import models


class Data(models.Model):
    ne = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    gsm = models.BooleanField()
    umts = models.BooleanField()
    lte = models.BooleanField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.ne
