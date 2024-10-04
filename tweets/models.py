from django.db import models

# Create your models here.


class Tweet(models.Model):
    # id = models.AutoField(primary_key=True) // how  primary key is created by django automatically
    content = models.TextField(blank=True, null=True)
    # Blank means it is not required in Django Forms, null means it can be empty in database as well
    image = models.FileField(upload_to="images/", blank=True, null=True)
