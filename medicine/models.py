# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class medicine(models.Model):
    medicine_name = models.CharField(max_length=50, primary_key='medicine_name')
    medicine_dosage = models.IntegerField()

    def __str__(self):
        return self.medicine_name


class disease(models.Model):
    disease_name = models.CharField(max_length=50,primary_key='disease_name')


    medicine_name = models.ForeignKey(medicine)

class symptoms(models.Model):
    symptoms_name = models.CharField(max_length=200)
    disease_name = models.ForeignKey(disease)




