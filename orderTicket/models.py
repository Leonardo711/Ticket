from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Train(models.Model):
    train_id = models.CharField(max_length=5, primary_key=True)
    train_type = models.CharField(max_length=1)
    num_station = models.IntegerField(default=-1)
    distance = models.FloatField(default=-1)

    def __str__(self):
        return self.train_id


class Station(models.Model):
    station_name = models.CharField(max_length = 30)
    train_come_by = models.ForeignKey(Train, on_delete=models.CASCADE)
    order_of_station = models.IntegerField(default = -1)
    arrive_time = models.CharField(max_length = 5)
    distance_count = models.FloatField(default = -1)
    
    def __str__(self):
        return self.station_name


class Price(models.Model):
    train_type = models.CharField(max_length=1) #T, D, G, Z, C, K..
    seat_type = models.CharField(max_length=10)
    price_per_km = models.FloatField(max_length=5)

class Seat(models.Model):
    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)
    carriage_id = models.IntegerField(default=-1)
    seat_type = models.CharField(max_length=10)
    seat_id = models.IntegerField(default = -1)
    date = models.DateField()
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.seat_type + '\t' + str(self.carriage_id) + '\t' +
                str(self.seat_id)


