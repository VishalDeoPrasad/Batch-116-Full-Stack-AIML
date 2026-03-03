from django.db import models
from django.utils import timezone

# Create your models here.
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    display_name = models.CharField()
    email = models.EmailField()
    contact = models.CharField()
    city = models.CharField()
    dob = models.DateField()
    password = models.CharField()
    image = models.ImageField(upload_to="images/profile_picture")
    joined_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.display_name
