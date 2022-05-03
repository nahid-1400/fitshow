from django import forms
from .models import CategoryCourse

category = CategoryCourse.objects.all()
category_choice = (
    ((cat.id, cat.title) for cat in category)
)

course_duration_choices = [
    ('30', 'یک ماهه'),
    ('90', 'سه ماهه'),
    ('180', 'شش ماهه'),
    ('365', 'یک ساله'),
]

class AddUserForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput, max_length=250)
    lastname = forms.CharField(widget=forms.TextInput, max_length=250)
    age = forms.CharField(widget=forms.NumberInput, max_length=3)
    mobile = forms.CharField(widget=forms.NumberInput, max_length=11)
    national_code = forms.CharField(widget=forms.NumberInput, max_length=10)
    category_course = forms.ChoiceField(choices=category_choice)
    course_duration = forms.ChoiceField(choices=course_duration_choices)


