from django.db import models

# Create your models here.

class Category(models.Model):
    """
       Model for category mapping
    """
    type = models.CharField(max_length=30,blank=True,null=True)
    value = models.CharField(max_length=30,blank=True,null=True)
      

class Movies(models.Model):
    """
       Model for movie Meta Data
    """
    title = models.CharField(max_length=90,blank=True,null=True)
    description = models.CharField(max_length=90,blank=True,null=True)
    movie_image = models.ImageField(upload_to="images/movies/")
    duration = models.IntegerField(default=0)
    release_date = models.DateField(blank=True,null=True,default=None)
    category = models.ManyToManyField(Category)
     
    

