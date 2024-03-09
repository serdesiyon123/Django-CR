from django.db import models
from django.contrib.auth.models import User

class DB(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    bio = models.TextField()
    image = models.ImageField(upload_to='templates/images')

    def __str__(self):
        return f"{self.name}" + f"{self.age}"
