from django.db import models

# Create your models here.
class Donate(models.Model):
    donor_id=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    amount=models.IntegerField(default=0)

    def __str__(self):
        return(self.name)

    