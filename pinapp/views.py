from django.shortcuts import render
from django.http  import HttpResponse
#from .models import Image

#views
'''
def welcome(request):
    return HttpResponse('Pintrest')
    '''

#pintresthomepageview
def welcome(request):
    return render(request, 'pintrest.html')
