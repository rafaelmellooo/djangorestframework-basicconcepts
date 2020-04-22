from django.db import models


class TouristAttraction(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    is_approved = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.name
