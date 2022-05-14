from django.db import models

# Create your models here.

class Films(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

class Session(models.Model):
    film = models.ForeignKey(
        Films,
        on_delete=models.CASCADE,
        related_name = 'arrivals'
        )
    time = models.DateTimeField()

    def __str__(self):
        return f'Movie {self.pk}: {self.film.name} at {self.time}'

class Payment(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} '


class Costumer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    sessions = models.ManyToManyField(Session)
    payment = models.ManyToManyField(Payment)

    def __str__(self):
        return f'{self.name} ({self.age})'