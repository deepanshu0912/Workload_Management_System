from django.db import models

class UserCredentials(models.Model):
    userid = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name = "UserCredential"
        verbose_name_plural = "UserCredentials"

    def __str__(self):
        return self.mobile
    
class User(models.Model):
    user = models.ForeignKey(UserCredentials)
    name = models.CharField(max_length=255)
    usertype = models.CharField()
