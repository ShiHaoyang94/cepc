# Generated by Django 2.2.27 on 2023-03-05 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TripCardRecords',
            fields=[
                ('ifnormal', models.CharField(db_column='IFNORMAL', max_length=255)),
                ('r_location', models.CharField(db_column='R_LOCATION', max_length=255)),
                ('student_num', models.CharField(db_column='STUDENT_NUM', max_length=255)),
                ('creation_time', models.DateTimeField(db_column='CREATION_TIME')),
                ('handle', models.CharField(db_column='HANDLE', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'trip_card_records',
                'managed': False,
            },
        ),
    ]
