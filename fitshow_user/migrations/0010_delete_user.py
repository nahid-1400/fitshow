# Generated by Django 4.0.4 on 2022-05-04 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitshow_user', '0009_alter_user_course_validity_up_to_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]