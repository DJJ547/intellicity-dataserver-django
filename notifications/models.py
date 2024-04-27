from django.db import models

class Notification(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    source_id = models.IntegerField(null=False)
    description = models.CharField(max_length=45)
    timestamp = models.DateTimeField(null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    source_type = models.CharField(max_length=45, null=False)
    dist_id = models.IntegerField(null=False)

    class Meta:
        db_table = 'notifications'
