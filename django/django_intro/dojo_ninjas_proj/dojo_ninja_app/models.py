from django.db import models
    
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()

    def __repr__(self):
        return f'< Dojo ID {self.id}: {self.name} >'


class Ninja(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)

    def __repr__(self):
        return f'< Ninja ID {self.id}: {self.first_name} >'