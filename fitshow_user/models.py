from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
from django.db.models import Q




class CategoryCourse(models.Model):
    title = models.CharField(default=None, max_length=250, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='عنوان در url')
    status = models.BooleanField(default=True, verbose_name='وضعیت')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی دوره'
        verbose_name_plural = 'دسته بندی دورها'




class FitShowUserManager(models.Manager):


    # ماژول جستوجو
    def search(self, query):
        lookup = (
            Q(fullname__icontains=query)|
            Q(firstname__icontains=query)|
            Q(lastname__icontains=query)|
            Q(national_code__icontains=query)|
            Q(phone__icontains=query)|
            Q(course_duration__icontains=query)
        )

        return self.get_queryset().filter(lookup).distinct()


course_duration_choices = [
    ('30', 'یک ماهه'),
    ('90', 'سه ماهه'),
    ('180', 'شش ماهه'),
    ('365', 'یک ساله'),
]


class FitShowUser(models.Model):
    fullname = models.CharField(max_length=125, default=None)
    firstname = models.CharField(max_length=125, default=None)
    lastname = models.CharField(max_length=125, default=None)
    phone = models.CharField(max_length=11, verbose_name='شماره موبایل', unique=True, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True, verbose_name='سن')
    national_code = models.CharField(max_length=10, blank=True, null=True, unique=True, verbose_name='کد ملی')
    category_course = models.ManyToManyField(CategoryCourse, blank=True, null=True, related_name='category_course_user', verbose_name='دوره کاربر')
    course_duration = models.CharField(choices=course_duration_choices, max_length=3, blank=True, null=True, default=None, verbose_name='مدت زمان دوره')
    course_validity_up_to_date = models.DateTimeField(default=timezone.now(), verbose_name='اعتبار دوره تا تاریخ')

    objects = FitShowUserManager()
    def __str__(self):
        return self.fullname

    # روزهای باقی مانده تا پایان دوره
    def day_to_end_course(self):
        end_course_day = self.course_validity_up_to_date - timezone.now()
        return end_course_day.days

    #  اپدیت تاریخ پایان دوره
    def course_validity_up_to_date_update(self):
        return self.course_validity_up_to_date + datetime.timedelta(days=int(self.course_duration))


    class Meta:
        verbose_name = 'کاربر فیت شو'
        verbose_name_plural = 'کاربران فیت شو'







