from django.db import models

class Species(models.Model):
    tree_species_id = models.IntegerField(primary_key=True)
    latin_name = models.CharField(max_length=100)

class FieldData(models.Model):
    class HealthChoices(models.IntegerChoices):
        Poor = 1
        Ok = 2
        Excellent = 3
        NA = 4
    individual_tree_id = models.IntegerField(primary_key=True)
    species_id = models.ForeignKey(Species, on_delete=models.CASCADE)
    method = models.CharField(max_length=50)
    height = models.IntegerField()
    health = models.IntegerField(choices=HealthChoices.choices)
    year_monitored = models.CharField(max_length=4)