from django.db import models
from django.conf import settings

# Create your models here.

class Goober(models.Model):
    name = models.CharField(max_length=100)
    health = models.IntegerField(default=0)
    image_url = models.URLField(blank=True)
    equipped_clothing = models.CharField(max_length=100, blank=True)
    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="goobers"
    )

    def __str__(self):
        return self.name