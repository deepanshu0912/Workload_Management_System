from django.urls import path
from .views import (GetFoodItemsView)

urlpatterns = [
    path('food_items/', GetFoodItemsView.as_view(), name='get_food_items'),
]