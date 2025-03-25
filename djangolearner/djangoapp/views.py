from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def json_view(request):
    return JsonResponse({'message': 'Hello, JSON!'})