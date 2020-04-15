from django.db import models
import uuid
from django.contrib.auth.models import User

#Project Model
class Project(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    name                = models.CharField(max_length=255)
    duration            = models.CharField(max_length=255)
    description         = models.TextField(null=True, blank = True)
    avatar              = models.FileField(upload_to='project/avatar/', null=True, blank = True)
    createdAt           = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt           = models.DateTimeField(auto_now=True, null=True)
    
    def __int__(self):
        return self.id
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

#Task Model
class Task(models.Model):
    project             = models.ForeignKey(Project, on_delete=models.CASCADE)
    name                = models.CharField(max_length=255)
    start_date          = models.DateField()
    end_date            = models.DateField()
    description         = models.TextField(null=True, blank = True)
    assign              = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    createdAt           = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt           = models.DateTimeField(auto_now=True, null=True)
    
    
    def __int__(self):
        return self.id
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

#Sub Task Model
class Subtask(models.Model):
    task                = models.ForeignKey(Task, on_delete=models.CASCADE)
    name                = models.CharField(max_length=255)
    start_date          = models.DateField()
    end_date            = models.DateField()
    description         = models.TextField(null=True, blank = True)
    createdAt           = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt           = models.DateTimeField(auto_now=True, null=True)
    
    def __int__(self):
        return self.id
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Subtask'
        verbose_name_plural = 'Subtasks'
        
