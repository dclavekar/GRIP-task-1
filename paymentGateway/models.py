from django.db import models

# Create your models here.
class Donate(models.Model):
    name=models.CharField(max_length=100)
    # phone=models.IntegerField()
    email=models.EmailField( max_length=254)
    amount=models.IntegerField(default=0)
    # paid=models.BooleanField(default=False)

    def __str__(self):
        return(self.name)

    