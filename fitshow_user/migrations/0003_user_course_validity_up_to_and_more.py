# Generated by Django 4.0.4 on 2022-05-03 07:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fitshow_user', '0002_user_age_user_course_duration_user_national_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course_validity_up_to',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 7, 15, 22, 980585, tzinfo=utc), verbose_name='مدت زمان دوره تا'),
        ),
        migrations.AlterField(
            model_name='user',
            name='course_duration',
            field=models.CharField(blank=True, choices=[('30', 'یک ماهه'), ('90', 'سه ماهه'), ('180', 'شش ماهه'), ('365', 'یک ساله')], default=None, max_length=3, null=True, verbose_name='مدت زمان دوره'),
        ),
    ]
