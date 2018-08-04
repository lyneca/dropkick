from django.db import models

# Create your models here.
class Unit(models.Model):
  unit_name = models.CharField(max_length=20)
  # Capture the unit name that is at the end of the path.
