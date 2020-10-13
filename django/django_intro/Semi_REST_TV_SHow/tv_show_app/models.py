from django.db import models
from datetime import date, datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors['title'] = "Show title should be at least 2 characters long"
        if Show.objects.filter(title = postData['title']).exists():
            errors['title'] = "This TV show already exists"
        if len(postData['network']) < 3:
            errors['network'] = "Show network should be at least 3 characters"   
        if len(postData['desc']) < 10:
            errors['desc'] = "Show description should be at least 10 characters"
        if len(postData['release_date']) == 0 or datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.today():
            errors['release_date'] = "The release date should be a valid date and in the past"
        return errors
        
class Show(models.Model):
    title = models.CharField(max_length=255) 
    desc = models.TextField()
    network = models.CharField(max_length=255)
    r_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    def __repr__(self):
        return f'< Show ID {self.id}: {self.title} >'