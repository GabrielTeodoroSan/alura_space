from django.db import models
from datetime import datetime

# Create your models here.

class Photographs(models.Model):

    category_choices = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    name = models.CharField(max_length=30, null=False, blank=False)
    legend = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.CharField(max_length=20, choices=category_choices, default="")
    photo = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
    published = models.BooleanField(default=False)
    date_photo = models.DateField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.name
