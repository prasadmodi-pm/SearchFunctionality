# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.context_processors import csrf
from .models import medicine
from .filters import UserFilter


# Create your views here.
def index(request):
    return HttpResponse('Hello this is medicine database')

def store(request):
    c ={}
    c.update(csrf(request))

    if request.method == 'POST':

        print (request.POST)

        t = request.POST['medicine_name']
        print (t)

        d = request.POST['medicine_dosage']
        print (d)

        b = medicine(medicine_name = t, medicine_dosage = d)
        b.save()

        return HttpResponse("data saved")
    else:
        return render(request,"form.html",c)


def search(request):
    user_list = medicine.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'searchform.html/', {'filter': user_filter})