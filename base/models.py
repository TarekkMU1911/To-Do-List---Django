from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Task(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to the user who created the task
    title = models.CharField(max_length=200)  # Title of the task
    description = models.TextField(null=True, blank=True)  # Description of the task
    complete = models.BooleanField(default=False)  # Status of the task
    create =  models.DateTimeField(auto_now_add=True)  # Timestamp when the task was created

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']