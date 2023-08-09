from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=32)
    nationality = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Mobile(models.Model):
    #color_choices=[('Black', 'Black'), ('White', 'White'), ('Gold', 'gold'), ('Silver', 'Silver'), ('Blue', 'Blue'),]
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=32, default='Mi 11X', unique=True)
    price = models.PositiveIntegerField(default=800)
    color = models.CharField(max_length=16, default='Blue')
    #color = models.CharField(choices=color_choices, default='Blue')
    display_size = models.FloatField(default=6.5)
    is_available = models.BooleanField(default=True)
    made_in = models.CharField(max_length=20, default='China')

    def __str__(self):
        return '{} {}'.format(self.brand.name, self.model)
