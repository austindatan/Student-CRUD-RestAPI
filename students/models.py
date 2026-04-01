from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    year_level = models.IntegerField()

    def __str__(self):
        return self.full_name # 8 spaces or 2 tabs total from the left margin