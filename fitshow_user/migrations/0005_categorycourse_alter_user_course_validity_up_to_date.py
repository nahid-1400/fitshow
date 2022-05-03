# Generated by Django 4.0.4 on 2022-05-03 15:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fitshow_user', '0004_remove_user_course_validity_up_to_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=250)),
                ('slug', models.URLField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='course_validity_up_to_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 15, 41, 3, 67634, tzinfo=utc), verbose_name='اعتبار دوره تا تاریخ'),
        ),
    ]
