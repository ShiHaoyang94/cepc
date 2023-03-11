from django.db import models

# Create your models here.
class AllUser(models.Model):
    privileges = models.CharField('权限等级',db_column='PRIVILEGES', max_length=255)  # Field name made lowercase.
    name = models.CharField('姓名',db_column='NAME', max_length=255)  # Field name made lowercase.
    student_num = models.CharField('账号',db_column='STUDENT_NUM', primary_key=True, max_length=255)  # Field name made lowercase.
    id_num = models.CharField('身份证号码',db_column='ID_NUM', max_length=255)  # Field name made lowercase.
    college_name = models.CharField('学院',db_column='COLLEGE_NAME', max_length=255)  # Field name made lowercase.
    class_name = models.CharField('班级',db_column='CLASS_NAME', max_length=255)  # Field name made lowercase.
    phone = models.CharField('电话',db_column='PHONE', max_length=255)  # Field name made lowercase.
    campus = models.CharField('校区',db_column='CAMPUS', max_length=255)  # Field name made lowercase.
    email = models.CharField('邮箱',db_column='EMAIL', max_length=255)  # Field name made lowercase.
    user_type = models.CharField('用户类型',db_column='USER_TYPE', max_length=255)  # Field name made lowercase.
    password = models.CharField('密码',db_column='PASSWORD', max_length=255,null=True,blank=True)  # Field name made lowercase.
    is_active = models.BooleanField('有效性',db_column='IS_ACTIVE', default=True)
    class Meta:
        managed = False
        db_table = 'all_user'
        verbose_name = '用户明细维护'
        verbose_name_plural = verbose_name

