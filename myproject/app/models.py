from django.db import models

# Create your models here.
class Title(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Registration(models.Model):
    reg_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    parent_id = models.IntegerField(null=True,blank=True)
    points = models.FloatField(null=True,blank=True)
   
    def __str__(self):
        return self.first_name

