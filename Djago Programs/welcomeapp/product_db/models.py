from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField   # auto increment 
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField()

    def __str__(self):
        #return str(self.id)+", "+self.product_name
        return self.product_name