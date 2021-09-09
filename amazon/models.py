from django.db import models

# Create your models here.
class catagory(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class product(models.Model):
    product=models.CharField(max_length=100)
    img=models.CharField(max_length=100)
    disc=models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    branch=models.ForeignKey(catagory,on_delete=models.CASCADE)
    def __str__(self):
        return self.product

