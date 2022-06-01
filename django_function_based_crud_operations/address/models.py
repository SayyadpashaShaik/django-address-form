from django.db import models

# Create your models here.

#address model to save the address of the customer

class Address(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.IntegerField()
    pincode = models.IntegerField()
    state = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    locality = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    Address_choices = (
        ('Home','Home'),
        ('Office','Office')
    )
    type_of_address = models.CharField(choices=Address_choices,max_length=20)

    def __str__(self):
        return self.name
