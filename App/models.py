from django.db import models
from django.utils import timezone

class Student(models.Model):

    GENDER = (
        ('남','남'),
        ('여','여'),
    )

    GRADE = (
        ('초','초'),   
        ('중','중'),   
        ('고','고'),   
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dateofbirth = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, null=True, choices=GENDER)
    grade = models.CharField(max_length=10, null=True, choices=GRADE)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name