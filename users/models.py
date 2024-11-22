from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
      
    @staticmethod
    def aunthenticate(username, password):
        try:
            try:
              user = User.objects.get(username=username)
            except User.DoesNotExist:
              user = User.objects.get(email=username)
            if check_password(password, user.password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
