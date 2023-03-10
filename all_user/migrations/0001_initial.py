# Generated by Django 2.2.27 on 2023-03-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllUser',
            fields=[
                ('privileges', models.CharField(blank=True, db_column='PRIVILEGES', max_length=255)),
                ('name', models.CharField(db_column='NAME', max_length=255)),
                ('student_num', models.CharField(db_column='STUDENT_NUM', max_length=255, primary_key=True, serialize=False)),
                ('id_num', models.CharField(db_column='ID_NUM', max_length=255)),
                ('college_name', models.CharField(db_column='COLLEGE_NAME', max_length=255)),
                ('class_name', models.CharField(blank=True, db_column='CLASS_NAME', max_length=255)),
                ('phone', models.CharField(blank=True, db_column='PHONE', max_length=255,)),
                ('campus', models.CharField(db_column='CAMPUS', max_length=255)),
                ('email', models.CharField(db_column='EMAIL', max_length=255)),
                ('user_type', models.CharField(db_column='USER_TYPE', max_length=255)),
                ('password', models.CharField(db_column='PASSWORD', max_length=255,null=True)),
            ],
            options={
                'db_table': 'all_user',
                'managed': False,
            },
        ),
    ]
