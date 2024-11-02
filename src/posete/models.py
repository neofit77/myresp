from django.db import models

# Create your models here.
class Gost(models.Model):
    ime = models.TextField(blank=True)
    prezime = models.TextField()
    godina_rodjenja = models.IntegerField()
    datum_prijave = models.DateTimeField(auto_now_add=True)