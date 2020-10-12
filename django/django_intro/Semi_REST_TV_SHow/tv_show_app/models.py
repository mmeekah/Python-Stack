from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255) 
    desc = models.TextField()
    network = models.CharField(max_length=255)
    r_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'< Show ID {self.id}: {self.title} >'