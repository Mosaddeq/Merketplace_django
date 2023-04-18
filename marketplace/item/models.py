from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural ='Categories'

    def __str__(self) :
        return self.name

# Define the PRICE_UNIT_CHOICES tuple outside of the Item class
PRICE_UNIT_CHOICES = (
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('GBP', 'GBP'),
    # Add more units as needed
)

class Item(models.Model):
    name= models.CharField(max_length=255) 
    description = models.TextField()
    price = models.FloatField(blank=True,null= True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name= 'items',on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name= 'items',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=  "item_img",blank=True,null=True)
    price_unit = models.CharField(max_length=50, choices=PRICE_UNIT_CHOICES, default='USD')  # Use the choices parameter


    class Meta:
        ordering = ('name',)
        #verbose_name_plural ='Categories'

    def __str__(self) :
        return self.name
