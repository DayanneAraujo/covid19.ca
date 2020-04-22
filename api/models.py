from django.db import models

class Covid19Ca(models.Model):
    date = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    pruid = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    prname = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    prnameFR = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    numconf = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    numprob = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    numdeaths = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    numtotal = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    numtested = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    numrecover = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    percentrecover = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    ratetested = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    numtoday = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
    percentoday = models.CharField(
        max_length=32, blank=True, null=True, default=None
    )
