from django.db import models

class SpdSelectAll(models.Model):
    ID = models.CharField(max_length=255, primary_key=True)
    Incident_Num = models.IntegerField()
    Incident_Type = models.CharField(max_length=255)
    Occured_date_time = models.DateField()
    Precinct = models.CharField(max_length=255)
    Sector = models.CharField(max_length=255)
    Beat = models.CharField(max_length=255)
    Officer_ID = models.IntegerField()
    Subject_ID = models.IntegerField()
    Subject_Race = models.CharField(max_length=255)
    Subject_Gender = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'spd'