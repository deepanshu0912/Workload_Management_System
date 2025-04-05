from django.db import models
from User.models import User

class Food_Items(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=255)
    food_type = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.food_type + " " + self.food_name
    
    class Meta:
        verbose_name = "Food_Item"
        verbose_name_plural = "Food_Items"

class Chef_Role(models.Model):
    id = models.AutoField(primary_key=True)
    chef = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(Food_Items, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Chef_Role"
        verbose_name_plural = "Chef_Roles"