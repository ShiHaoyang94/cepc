from django.db import models

# Create your models here.
class TripCardRecords(models.Model):
    ifnormal = models.CharField(db_column='IFNORMAL',max_length=255)  # Field name made lowercase.
    r_location = models.CharField(db_column='R_LOCATION', max_length=255)  # Field name made lowercase.
    student_num = models.CharField(db_column='STUDENT_NUM',  max_length=255)  # Field name made lowercase.
    creation_time = models.DateTimeField(db_column='CREATION_TIME')  # Field name made lowercase.
    handle = models.CharField(db_column='HANDLE', max_length=255, primary_key=True)

    class Meta:
        managed = False
        db_table = 'trip_card_records'
