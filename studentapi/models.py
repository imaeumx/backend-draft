from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year_level = models.IntegerField()

    def __str__(self):
        return f"{self.full_name} - {self.course} (Year {self.year_level})"