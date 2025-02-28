from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Degree(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=200)
    numberOfYear = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(4)]) 

    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    age = models.IntegerField(validators=[MaxValueValidator(2010),MinValueValidator(1970)])
    slug = models.SlugField(db_index=True, blank=True)
    finishedDegree = models.BooleanField(default=True)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE,related_name="fkstudents")
    def __str__(self):
        return f'{self.name} {self.surname}'
    
    def get_absolute_url(self):
        return reverse("student-detail", args=[self.slug])
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
