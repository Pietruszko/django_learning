from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import sqlite3
from .models import Item
from .models import Todo, Category
import json
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        data =json.loads(request.body)
        new_todo = Todo(title=data['title'], description=data['description'])
        new_todo.save()
        return JsonResponse({'message': 'Todo added successfully'}, status = 201)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)
    
@csrf_exempt
def add_category(request):
    if request.method == 'POST':
        data =json.loads(request.body)
        new_category = Category(name=data['name'])
        new_category.save()
        return JsonResponse({'message': 'Category added successfully'}, status = 201)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def add_todo_with_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        category = Category.objects.get(name=data['name'])
        new_todo = Todo(title=data['title'],
         description=data['description'], category=category)
        new_todo.save()
        return JsonResponse({'message': 'Todo with category added successfully'}, status = 201)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)
        
    
def check_todo(request):
    todos = Todo.objects.select_related('category').all()

    result = []
    for todo in todos:
        result.append({
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'completed': todo.completed,
            'category_name': todo.category.name if todo.category else None
        })
    return JsonResponse({'todos': result})
