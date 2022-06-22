from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class User(AbstractUser):
      bio = models.CharField(max_length=100, null=True, blank=True)
      pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
      web = models.URLField(null=True, blank=True)
      is_verified = models.BooleanField(default=False)
      

      def get_absolute_url(self):
        return reverse('home')

      def __str__(self):
        return str(self.username) 
      
class Friend(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')  
  friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
  unread = models.PositiveIntegerField(default=0, )

  def __str__(self):
        return str(self.friend)
  




