from django.db import models

class Single(models.Model):
    Surname = models.CharField(max_length=64)
    Name = models.CharField(max_length=64)
    FatherName = models.CharField(max_length=64)
    Email = models.EmailField(max_length=64)
    Country = models.CharField(max_length=64)
    City = models.CharField(max_length=64)
    DateOfBirth = models.DateField()
    PhoneNumber = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.Surname} {self.Name}🐦‍⬛"


class CyberSport(Single):
    Game = models.CharField(max_length=64)
    ParticipateFormat = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.Surname} {self.Name} - {self.Game}"


class Hackathon(Single):
    course = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.Surname} {self.Name} - {self.course}"


class Design(Single):
    course = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.Surname} {self.Name} - {self.course}"


class Mobilography(Single):
    pass

class Robotix(Single):
    pass

class DroneRace(Single):
    pass

class Speaker(Single):
    speech_theme = models.CharField(max_length=255)

class MasterClass(Single):
    speech_theme = models.CharField(max_length=255)