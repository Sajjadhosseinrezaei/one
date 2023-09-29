from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField()

class Person(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    number = models.IntegerField()

