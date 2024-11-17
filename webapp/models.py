from django.db import models
import os

class Users(models.Model):
  name = models.CharField(max_length=255, null=True)
  email = models.EmailField(max_length=255, unique=True)
  password = models.CharField(max_length=255, null=True)


class Images(models.Model):
    path1 = models.ImageField(upload_to='webapp/static/image1')
    path2 = models.ImageField(upload_to='webapp/static/image2')

    def path1_filename(self):
        return os.path.basename(self.path1.name)

    def path2_filename(self):
        return os.path.basename(self.path2.name)
    

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

