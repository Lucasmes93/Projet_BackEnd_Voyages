from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Meta:
        app_label = 'recommendations'
        db_table = 'userprofile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username


class Destination(models.Model):
    class Meta:
        app_label = 'recommendations'
        db_table = 'destinations'

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    class Meta:
        app_label = 'recommendations'
        db_table = 'bookings'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.destination.name}"

    def clean(self):
        from django.core.exceptions import ValidationError
        from datetime import date
        if self.date < date.today():
            raise ValidationError("La date de réservation ne peut pas être dans le passé.")
