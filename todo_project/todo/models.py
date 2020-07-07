from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
    