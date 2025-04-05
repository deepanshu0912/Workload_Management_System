from django.db import models
from User.models import User
from Food.models import Food_Items

class Orders(models.Model):
    status_choices = [('New', 'New'),
                      ('Preparing', 'Preparing'),
                      ('Completed', 'Completed')]
    
    order_id = models.CharField(max_length=255, primary_key=True)
    order_channel = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=status_choices)
    timestamp = models.BigIntegerField()

    def __str__(self):
        return self.order_id
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

class Order_Items(models.Model):
    status_choices = [('Completed', 'Completed'),
                    ('Processing', 'Processing'),
                    ('Pending', 'Pending')]
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    food_item = models.ForeignKey(Food_Items, on_delete=models.CASCADE)
    number_of_items = models.IntegerField()
    status = models.CharField(max_length=255, choices = status_choices)

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = "Order_Item"
        verbose_name_plural = "Order_Items"
