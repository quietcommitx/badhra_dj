from select import select

from django.db import models

# Create your models here.
# Todolist/Note
# title           String
# description     String
# is_completed    Boolean
# created_date    Date/DateTime
# completed_date  Date/DateTime

class Todolist(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField(null=True, blank=True)
   is_completed = models.BooleanField(default=False)
   create_date = models.DateField(auto_now=True)

   def __str__(self):
      return self.title



# Get data from Table
# select * from Todolist;    (sql command)
# models file: 
#    class/Table define 
# -> migration file (python manage.py makemigrations)
# -> database reflect (python manage.py migrate)