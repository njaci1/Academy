from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    #creating relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional use UserAttributes
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.username
