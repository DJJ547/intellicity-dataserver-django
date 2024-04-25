from django.db import models

class Camera(models.Model):
    id = models.IntegerField(unique=True, null=False, primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    index = models.IntegerField(unique=True, null=False)
    time = models.DateTimeField()
    image_url = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.IntegerField()
    enabled = models.SmallIntegerField()

    class Meta:
        db_table = 'cameras'
        
class Iot(models.Model):
    station_id = models.IntegerField(primary_key=True, null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    address = models.CharField(max_length=48)
    district = models.IntegerField(null=False)
    hourlySpeed = models.CharField(max_length=512)
    enabled = models.SmallIntegerField()

    class Meta:
        db_table = 'iots'
        
class Drone(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()
    status = models.CharField(max_length=45)
    dist_id = models.CharField(max_length=12)
    timestamp = models.DateTimeField()
    video_url = models.CharField(max_length=500)

    class Meta:
        db_table = 'drones'
