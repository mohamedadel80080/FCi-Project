from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=10, null=False)
    major = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.username


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username
