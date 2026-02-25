from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    mobile = models.CharField()
    email = models.EmailField()

    def __str__(self):
        return self.name