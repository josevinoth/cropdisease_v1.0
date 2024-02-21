# main/models.py
from django.db import models

class UserQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    query = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class DoctorSuggestion(models.Model):
    query = models.ForeignKey(UserQuery, on_delete=models.CASCADE)
    suggestion = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Registration(models.Model):
    USER_TYPES = [
        ('Farmer', 'Farmer'),
        ('Doctor', 'Doctor'),
        ('Government Official', 'Government Official'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return self.name
