from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

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