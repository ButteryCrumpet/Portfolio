from django.db import models

TYPE_CHOICES = (('Frontend','Frontend'), ('Backend','Backend'), ('Legacy','Legacy'), ('Coding','Coding'),)

class Project(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    technologies = models.ManyToManyField('Technology')
    description = models.TextField()
    link = models.CharField(max_length=200)
    git_link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class AdditionalImage(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey('Project')
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
