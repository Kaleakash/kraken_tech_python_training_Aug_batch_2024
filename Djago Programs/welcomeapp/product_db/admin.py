from django.contrib import admin
from .models import Product;
# Register your models here.

admin.site.register(Product)    # after register we can view product table in 
                                # admin dashboard 