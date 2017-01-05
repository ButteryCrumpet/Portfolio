from django.db import models

TYPE_CHOICES = (('Frontend','Frontend'), ('Backend','Backend'), ('Legacy','Legacy'), ('Coding','Coding'),)
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    languages = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name
