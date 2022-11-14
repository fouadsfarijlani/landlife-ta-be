from django.db import models

class FieldData(models.Model):
    class HealthChoices(models.Model):
        Poor = 1
        Ok = 2
        Excellent = 3
        NA = 4
    individual_tree_id = models.IntegerField(primary_key=True)
    species_id = models.IntegerField()
    method = models.CharField(max_length=50)
    height = models.IntegerField()
    health = models.IntegerChoices(choices = HealthChoices)
    year_monitored = models.CharField(max_length=4)