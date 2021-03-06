# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..adoption.models import Person
# Create your models here.


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)


class Pet(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    approximated_age = models.IntegerField()
    rescue_date = models.DateField()
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    vaccine = models.ManyToManyField(Vaccine, blank=True)


