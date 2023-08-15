from django.db import models

prefix_chioces = (

)

class Author(models.Model):

    prefix_chioces = ()
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    
    
