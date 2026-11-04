from django.urls import path
from .views import * 

urlpatterns = [
   path('home/', home),
   path('aboutus/', aboutus),
   path('todolist/', todolist),
   path('create/', create),
   path('todolist/<id>/', edit),
   path('todolist/<id>/mark/', mark_complete)
]
