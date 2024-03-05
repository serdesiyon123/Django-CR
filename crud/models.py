from django.db import models

class DB(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    bio = models.TextField()
    image = models.ImageField(upload_to='templates/images')
