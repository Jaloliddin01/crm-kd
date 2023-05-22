from django.db import models

# Create your models here.

class Staff(models.Model):
    UNVON = (
        ('Direktor', 'Direktor'),
        ("Katta o'qituvchi", "Katta o'qituvchi"),
        ("Oshpaz", "Oshpaz"),
        ("Qorovul", "Qorovul"),
        ("Kichik o'qituvchi", "Kichik o'qituvchi")
    )
    FISH = models.CharField(max_length=100)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=100)
    millati = models.CharField(max_length=50)
    unvoni = models.CharField(max_length=50, choices=UNVON)

    def __str__(self):
        return self.FISH

class Child(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=100)
    millati = models.CharField(max_length=50)
    yoshi = models.FloatField()
    gruppasi = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=50)
    davomiyligi = models.FloatField()
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    