from django.db import models

# Create your models here.
class AllUser(models.Model):
    privileges = models.CharField(db_column='PRIVILEGES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    student_num = models.CharField(db_column='STUDENT_NUM', primary_key=True, max_length=255)  # Field name made lowercase.
    id_num = models.CharField(db_column='ID_NUM', max_length=255)  # Field name made lowercase.
    college_name = models.CharField(db_column='COLLEGE_NAME', max_length=255)  # Field name made lowercase.
    class_name = models.CharField(db_column='CLASS_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    campus = models.CharField(db_column='CAMPUS', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255)  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=255)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='IS_ACTIVE', default=True)
    class Meta:
        managed = False
        db_table = 'all_user'


