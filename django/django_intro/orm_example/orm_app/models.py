from django.db import models

class Star(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'< Star ID {self.id}: {self.name} >'

class Planet(models.Model):
    name = models.CharField(max_length=45)
    system_star = models.ForeignKey(Star, related_name="system_planets", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'< Planet ID {self.id}: {self.name} >'