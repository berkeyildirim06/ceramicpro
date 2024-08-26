from django.db import models

class Warranty(models.Model):
    CAR_TYPES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('truck', 'Truck'),
    ]

    car_type = models.CharField(max_length=100, choices=CAR_TYPES, default='sedan')
    
    # Front side measurements and image
    front_marked_image = models.CharField(max_length=255, null=True, blank=True)
    front_before_base_coat = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    front_after_base_coat = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    front_after_top_coat = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    
    # Left side measurements and image
    left_marked_image = models.CharField(max_length=255, null=True, blank=True)
    left_before_base_coat = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    left_after_base_coat = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    left_after_top_coat = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    
    # Back side measurements and image
    back_marked_image = models.CharField(max_length=255, null=True, blank=True)
    back_before_base_coat = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    back_after_base_coat = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    back_after_top_coat = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)