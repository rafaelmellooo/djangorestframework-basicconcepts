from django.db import models

from assessments.models import Assessment
from attractions.models import Attraction


class TouristAttraction(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    is_approved = models.BooleanField(blank=True, default=False)
    attractions = models.ManyToManyField(Attraction)
    assessments = models.ManyToManyField(Assessment)

    def __str__(self):
        return self.name
