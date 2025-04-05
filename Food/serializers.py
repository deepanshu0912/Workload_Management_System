from rest_framework import serializers
from .models import Food_Items

class Food_ItemsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Food_Items
        fields = [
            'food_id',
            'food_name',
            'food_type',
            'price'
        ]