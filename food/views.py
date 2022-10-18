from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('<h1>Food application</h1><h2>Home Page</h2>')
    var = {'name': 'Fast food', 'message': "Dzień dobry!"}
    return render(request, 'food/index.html', var)

def pizza(request):
    return render(request, 'food/pizza.html')
