"""
URL configuration for djangolearner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangoapp import views

handler404 = 'djangoapp.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('json/', views.json_view, name='json'),
    path('user/<str:name>/', views.http_view, name='http'),
    path('search/', views.query_view, name='search'),
    path('add-and-get/', views.add_and_get_items),
    path('add-todo/', views.add_todo, name='add-todo'),
    path('get/', views.check_todo, name='get-todo'),
    path('add-category/', views.add_category, name='add-category'),
    path('add-todo-with-category/', views.add_todo_with_category, name='add-todo-with-category'),
]
