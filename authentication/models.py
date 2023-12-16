from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    ...
    def delete(self, *args, **kwargs):
        super(Property, self).delete(*args, **kwargs)

#propery
class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    property_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    bathrooms = models.IntegerField()
    floors = models.IntegerField()
    garages = models.IntegerField()
    area = models.DecimalField(max_digits=8, decimal_places=2)
    sale_or_rent_price = models.DecimalField(max_digits=8, decimal_places=2)
    before_sale_label = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=8, decimal_places=2)
    after_sale_label = models.CharField(max_length=255)
    center_cooling = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    pet_friendly = models.BooleanField(default=False)
    barbeque = models.BooleanField(default=False)
    fire_alarm = models.BooleanField(default=False)
    modern_kitchen = models.BooleanField(default=False)
    storage = models.BooleanField(default=False)
    dryer = models.BooleanField(default=False)
    heating = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    sauna = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    dish_washer = models.BooleanField(default=False)
    emergency_exit = models.BooleanField(default=False)
    image = models.ImageField(upload_to='properties/')
    created_at = models.DateTimeField(auto_now_add=True)




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

