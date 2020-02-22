from django.db import models


class User(models.Model):
    name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Articles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Section = models.CharField(max_length=200)
    SubSection = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    article = models.TextField()

    def __str__(self):
        return self.title


class Guest(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    emailid = models.EmailField()

    def __str__(self):
        return self.name
