from django.db import models

from django.core.validators import MinValueValidator, MinLengthValidator

# Create your models here.
class Monument(models.Model):
    STYLE_CHOICES = [
        ('GO', 'Gothic'),
        ('RO', 'Romanesque'),
        ('BA', 'Baroque'),
        ('NE', 'Neoclassical'),
        ('MO', 'Modern'),
        ('OT', 'Other'),
    ]

    name = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    city = models.CharField(max_length=100)
    year_built = models.IntegerField()
    height = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.1)])
    is_unesco_heritage = models.BooleanField(default=False)
    style = models.CharField(max_length=20, choices=STYLE_CHOICES, default='OT')

    def __str__(self):
        return f"{self.name} ({self.city})"