# Generated by Django 4.0.4 on 2022-05-04 06:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fitshow_user', '0008_alter_user_course_validity_up_to_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='course_validity_up_to_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 6, 4, 0, 627405, tzinfo=utc), verbose_name='اعتبار دوره تا تاریخ'),
        ),
    ]
