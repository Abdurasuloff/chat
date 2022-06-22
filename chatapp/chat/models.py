from django.db import models
from users.models import User

# Create your models here.
class Chat(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    chat=models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    is_seen = models.CharField(default="&#10003;", max_length=150)
    def __str__(self):
        return str(self.sender)+' >>> '+str(self.receiver)

