from django.db import models

# Create your models here.
class AbnormalRecords(models.Model):
    location_c = models.CharField('所在城市',db_column='LOCATION_C', max_length=255)  # Field name made lowercase.
    temperature = models.CharField('温度',db_column='TEMPERATURE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    student_num = models.CharField('账号',db_column='STUDENT_NUM', max_length=255)  # Field name made lowercase.
    location_p = models.CharField('所在省份',db_column='LOCATION_P', max_length=255)  # Field name made lowercase.
    creation_time = models.DateTimeField('创建时间',db_column='CREATION_TIME')  # Field name made lowercase.
    abnormal_type = models.CharField('异常类型',db_column='ABNORMAL_TYPE', max_length=255)  # Field name made lowercase.
    abnormal_desc = models.CharField('异常描述',db_column='ABNORMAL_DESC', max_length=255)  # Field name made lowercase.
    bts_record = models.CharField('返校类型',db_column='BTS_RECORD',max_length=255)  # Field name made lowercase
    handle = models.CharField('主键',db_column='HANDLE', max_length=255,primary_key=True)  # Field name made lowercase
    is_sign = models.BooleanField('是否异常签到', db_column='IS_SIGN')
    college_name = models.CharField('学院', db_column='COLLEGE_NAME', max_length=255)  # Field name made lowercase.
    info = models.CharField('处理信息', db_column='INFO', max_length=255)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'abnormal_records'
        verbose_name = '上报异常维护'
        verbose_name_plural = verbose_name
