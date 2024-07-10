from django.db import models

class FoodZone(models.Model):
    Brand_name = models.CharField(max_length=100)
    Legal_name = models.CharField(max_length=100)
    Legal_address = models.CharField(max_length=100)
    INN = models.IntegerField()
    Supervisor_Name = models.CharField(max_length=100)
    Job_Title = models.CharField(max_length=100)
    Company_Activity = models.CharField(max_length=255)
    Web_Site = models.URLField(max_length=100)
    Email = models.EmailField(max_length=100)
    Country = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=100)
    Company_Product = models.CharField(max_length=255)
    Logo = models.ImageField(upload_to="logos/")
    Register_check = models.ImageField(upload_to="register_check/")


    def __str__(self):
        return self.Brand_name

class IT_Expo(FoodZone):
    Theme = models.CharField(max_length=100)