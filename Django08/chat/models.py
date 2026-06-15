from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=50, null=False)

class Messages(models.Model):
    text = models.TextField(null=False)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    submitted_at = models.DateTimeField(auto_now=False, auto_now_add=True)