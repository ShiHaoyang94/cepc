from django.db import models

# Create your models here.
class AbnormalRecords(models.Model):
    location_c = models.CharField(db_column='LOCATION_C', max_length=255)  # Field name made lowercase.
    temperature = models.CharField(db_column='TEMPERATURE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    student_num = models.CharField(db_column='STUDENT_NUM', max_length=255)  # Field name made lowercase.
    location_p = models.CharField(db_column='LOCATION_P', max_length=255)  # Field name made lowercase.
    creation_time = models.DateTimeField(db_column='CREATION_TIME')  # Field name made lowercase.
    abnormal_type = models.CharField(db_column='ABNORMAL_TYPE', max_length=255)  # Field name made lowercase.
    abnormal_desc = models.CharField(db_column='ABNORMAL_DESC', max_length=255)  # Field name made lowercase.
    bts_record = models.CharField(db_column='BTS_RECORD',max_length=255)  # Field name made lowercase
    handle = models.CharField(db_column='HANDLE', max_length=255,primary_key=True)  # Field name made lowercase


    class Meta:
        managed = False
        db_table = 'abnormal_records'
