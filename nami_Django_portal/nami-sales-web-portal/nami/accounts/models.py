from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=20)
    cr_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    select_resident = models.CharField(max_length=20)


    def __str__(self):
        return self.user.username


