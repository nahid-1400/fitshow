from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime



course_duration_choices = [
    ('30', 'یک ماهه'),
    ('90', 'سه ماهه'),
    ('180', 'شش ماهه'),
    ('365', 'یک ساله'),
]


class User(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name='شماره موبایل', unique=True, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True, verbose_name='سن')
    national_code = models.CharField(max_length=10, blank=True, null=True, verbose_name='کد ملی')
    # category = None
    course_duration = models.CharField(choices=course_duration_choices, max_length=3, blank=True, null=True, default=None, verbose_name='مدت زمان دوره')
    course_validity_up_to_date = models.DateTimeField(default=timezone.now(), verbose_name='اعتبار دوره تا تاریخ')

    #  اپدیت روز های زمان دوره
    def course_validity_up_to_date_update(self):
        return self.course_validity_up_to_date + datetime.timedelta(days=int(self.course_duration))

    # روزهای باقی مانده تا پایان دوره
    def day_to_end_course(self):
        end_course_day = self.course_validity_up_to_date - timezone.now()
        return end_course_day.days