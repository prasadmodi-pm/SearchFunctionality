# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import medicine,symptoms,disease

# Register your models here.
admin.site.register(medicine)
admin.site.register(symptoms)
admin.site.register(disease)