from django.db import models

class UserCredentials(models.Model):
    userid = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name = "UserCredential"
        verbose_name_plural = "UserCredentials"

    def __str__(self):
        return self.userid
    
class User(models.Model):
    user_type_choices = [('Customer', 'Customer'),
                    ('Chef', 'Chef')]
        
    id = models.AutoField(primary_key=True)
    user_credentials = models.ForeignKey(UserCredentials, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, unique=True)
    user_type = models.CharField(max_length=255, choices=user_type_choices)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.mobile