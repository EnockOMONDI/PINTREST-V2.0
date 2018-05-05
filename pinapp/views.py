from django.shortcuts import render
from django.http  import HttpResponse

#views
def welcome(request):
    return HttpResponse('Pintrest')
