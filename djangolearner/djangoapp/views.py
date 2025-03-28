from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import sqlite3
from .models import Item

# Create your views here.

def home(request):
    return render(request, 'home.html')

def json_view(request):
    return JsonResponse({'message': 'Hello, JSON!'})

def http_view(request, name):
    return HttpResponse(f'Hello, {name}!')

def query_view(request):
    query = request.GET.get('q', '')
    return HttpResponse(f'You searched for: {query}')

def custom_404(request, exception):
    return HttpResponse("Custom 404 Error", status=404)

def get_items(request):
    connection = sqlite3.connect('db.sqlite3')
    items = []
    try:
        raw_query = 'SELECT * FROM items'
        items = connection.execute(raw_query).fetchall()
    finally:
        connection.close()
    return JsonResponse({'items': items})

def add_and_get_items(request):
    item = Item(name='New Item')
    item.save()
    
    items = Item.objects.all()

    return HttpResponse(items)