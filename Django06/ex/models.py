from django.db import models

# Create your models here.

class Perm(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
  

class User(models.Model):
    username = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    perm = models.ManyToManyField(Perm, blank=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Tip(models.Model):
    content = models.TextField(blank=False, null=False)
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE)
    value = models.IntegerField()
