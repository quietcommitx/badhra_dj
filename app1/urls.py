from django.urls import path, re_path
from django.shortcuts import redirect
from .views import * 

urlpatterns = [
   path('home/', home),
   path('aboutus/', aboutus),
   path('todolist/', todolist),
   path('create/', create),
   path('todolist/<id>/', edit),
   path('todolist/<id>/mark/', mark_complete),
   
   re_path(r'^.*$', lambda request: redirect('todolist/'))
]
