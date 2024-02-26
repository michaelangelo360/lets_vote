from django.db import models

# Create your models here.

class Candidate (models.Model):
    name = models.CharField(max_length= 200)
    email =models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Event (models.Model):
    name = models.CharField(max_length=200)



    def __str__(self):
        return self.name



class Category (models.Model):

    name = models.CharField(max_length= 200)
    event = models.ForeignKey('Event',on_delete= models.CASCADE)


    def __str__(self):
        return self.name


class Statistic (models.Model):

    total_number = models.IntegerField()
    name_of_stat = models.CharField(max_length = 200)

    def __str__(self):
        return self.name_of_stat
