from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name

class Add(models.Model):
  author = models.CharField(max_length=50 , null=True ,blank=True )
  moveName = models.CharField(max_length=50 , null=True ,blank=True)
  moveImage = models.ImageField(upload_to='photo' , null=True ,blank=True)
  movesumarize = models.TextField(null=True ,blank=True)
  viewers = models.IntegerField(null=True ,blank=True)
  rating = models.DecimalField(max_digits=2 , decimal_places=1 ,null=True ,blank=True)
  date = models.DateField(null=True , blank=True)
  category = models.ForeignKey(Category , on_delete=models.CASCADE,null=True ,blank=True)
  def __str__(self):
    return self.moveName