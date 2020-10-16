from django.db import models

# Create your models here.

# from django.db import models

"""
Nice sql designer tool at : https://ondras.zarovi.cz/sql/demo/
"""

class Artists(models.Model):
      name = models.CharField(max_length=200, unique=True)

class Albums(models.Model):
      artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
      reference = models.IntegerField(null=True)
      created_at = models.DateField(auto_now_add=True)
      available = models.BooleanField(default=True)
      title = models.CharField(max_length=200, unique=True)
      picture = models.URLField()

    
class Contact(models.Model):
      email = models.EmailField(max_length=100)
      name = models.CharField(max_length=200, unique=True)
class Booking(models.Model):
      created_at = models.DateField(auto_now_add=True)
      contacted = models.BooleanField(default=False)
      contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
      album = models.ForeignKey(Albums, on_delete=models.CASCADE)

ARTISTS = {
  'francis-cabrel': {'name': 'Francis Cabrel'},
  'lej': {'name': 'Elijay'},
  'rosana': {'name': 'Rosana'},
  'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}


ALBUMS = [
  {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
  {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]