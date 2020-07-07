from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
    
    def was_added_today(self):
        return self.date == timezone.now().date()
        

