from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20)
    event_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=50)

    def __str__(self):
        return self.name