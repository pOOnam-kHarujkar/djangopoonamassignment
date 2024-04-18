from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    username = models.CharField(db_index=True, unique=True, max_length=255)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.username


class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='assigned_projects')
    def __str__(self):
        return self.project_name
