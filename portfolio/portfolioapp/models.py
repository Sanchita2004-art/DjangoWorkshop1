from django.db import models

# Create your models here.
class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    year = models.DateField()

    def __str__(self):
        return f"{self.school} - {self.degree}"
    
class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    year = models.DateField()

    def __str__(self):
        return f"{self.company} - {self.position}"