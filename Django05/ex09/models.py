from django.db import models


class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.TextField(null=True, blank=True)
    diameter = models.PositiveIntegerField(null=True, blank=True)
    orbital_period = models.PositiveIntegerField(null=True, blank=True)
    population = models.PositiveBigIntegerField(null=True, blank=True)
    rotation_period = models.PositiveIntegerField(null=True, blank=True) 
    surface_water = models.FloatField(null=True, blank=True)
    terrain = models.TextField(null=True, blank=True) 
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,  auto_now_add=False)
    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    birth_year = models.CharField(max_length=32, null=True, blank=True) 
    gender = models.CharField(max_length=32)
    eye_color = models.CharField(max_length=32, null=True, blank=True)
    hair_color = models.CharField(max_length=32, null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True) 
    mass = models.FloatField(null=True, blank=True) 
    homeworld = models.ForeignKey(Planets, to_field='name', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,  auto_now_add=False)
    def __str__(self):
        return self.name
    