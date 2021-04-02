from django.db import models
class Region(models.Model):
    region_candidato = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Candidato(models.Model):
    candidato = models.ForeignKey(Region, on_delete=models.CASCADE)
    info_candidato = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

# Create your models here.
