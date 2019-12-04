from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    name=models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizer')
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(auto_now=True)
    attendances = models.ManyToManyField(User, through='Attendance')
    
    def __str__(self):
        return self.name

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.reviewer.username + " : " + self.event.name

class Attendance(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendances')
    event= models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendances')

    def __str__(self):
        return self.user.username + " : " + self.event.name

