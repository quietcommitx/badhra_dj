from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todolist
# Create your views here.

def home(request):
   people = [
      {
         "name":"John",
         "age":30,
         "address":"New York"
      },
      {
         "name":"Jane",
         "age":25,
         "address":"Los Angeles"
      },
      {
         "name":"Bob",
         "age":35,
         "address":"Chicago"
      },
      {
         "name":"Ram",
         "age":35,
         "address":"Chicago"
      }
   ]
   context = {
      "title":"abc",
      "heading":"Welcome",
      "content":"This is the content of the home page",
      "abc":people
   }
   return render(request, 'home.html', context)

def aboutus(request):
   return render(request, 'aboutus.html')
# aboutus, contactus create function and url


def todolist(request):
   queryset = Todolist.objects.all()   # return queryset: format same as people variable in home function
   completed = Todolist.objects.filter(is_completed = True).count()
   incomplete = Todolist.objects.filter(is_completed = False).count()
   context = {
      'tasks':queryset,
      'completed': completed,
      'incomplete': incomplete
   }
   return render(request, 'todolist.html', context)

def create(request):
   if request.method == 'POST':
      title = request.POST.get('title')
      description = request.POST.get('description')
      Todolist.objects.create(title = title, description=description)
   return render(request, 'create.html')

def mark_complete(request, id):
   task = Todolist.objects.get(id = id)
   # if is_completed is True -> False and if is_completed is False -> True
   task.is_completed = True
   task.save()
   return redirect('/todolist/')

def edit(request, id):
   task = Todolist.objects.get(id = id)
   if request.method == 'POST':
      title = request.POST.get('title')
      description = request.POST.get('description')
      task.title = title
      task.description = description
      task.save()
      return redirect('/todolist/')
   
   context = {'task':task}
   return render(request, 'edit.html',context)

# delete function, url, todolist page add Delete buttom