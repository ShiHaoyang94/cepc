from django.db import models

# Create your models here.
class TripCardRecords(models.Model):
    ifnormal = models.CharField('是否异常',db_column='IFNORMAL',max_length=255)  # Field name made lowercase.
    r_location = models.CharField('七日内行程',db_column='R_LOCATION', max_length=255)  # Field name made lowercase.
    student_num = models.CharField('账号',db_column='STUDENT_NUM',  max_length=255)  # Field name made lowercase.
    creation_time = models.DateTimeField('创建时间',db_column='CREATION_TIME')  # Field name made lowercase.
    handle = models.CharField('主键',db_column='HANDLE', max_length=255, primary_key=True)

    class Meta:
        managed = False
        db_table = 'trip_card_records'
        verbose_name = '行程异常维护'
        verbose_name_plural = verbose_name
