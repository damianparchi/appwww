import imp
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def say_hi(request):
    return HttpResponse('Cześć! To pierwszy widok!')

def say_secondtime(request):
    return render(request, 'sayhello.html', { 'name': 'Damian'})