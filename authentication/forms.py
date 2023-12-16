from django import forms
from .models import Property

#all propery
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'property_type', 'status', 'location', 'bathrooms', 'floors', 'garages', 'area', 'sale_or_rent_price', 'before_sale_label', 'size', 'after_sale_label', 'center_cooling', 'balcony', 'pet_friendly', 'barbeque', 'fire_alarm', 'modern_kitchen', 'storage', 'dryer', 'heating', 'pool', 'laundry', 'sauna', 'gym', 'elevator', 'dish_washer', 'emergency_exit', 'image']

