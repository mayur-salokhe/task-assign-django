from django.db import models

# Create your models here.
from django.contrib.auth.models import Group, User

group, created = Group.objects.get_or_create(name='TaskGroup')
group, created = Group.objects.get_or_create(name='NonTaskGroup')

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE)