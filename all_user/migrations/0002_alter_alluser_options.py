# Generated by Django 3.2.18 on 2023-03-11 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alluser',
            options={'managed': False, 'verbose_name': '用户明细维护', 'verbose_name_plural': '用户明细维护'},
        ),
    ]
