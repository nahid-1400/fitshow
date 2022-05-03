from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.utils import timezone

def home(request):
    user = request.user
    print(user.day_to_end_course())
    return HttpResponse()