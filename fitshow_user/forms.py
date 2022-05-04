from django import forms
from .models import CategoryCourse
from .models import FitShowUser
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


    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        fitshow_user = FitShowUser.objects.filter(phone=mobile).exists()
        if fitshow_user:
            raise forms.ValidationError('شماره تلفن وارد شده تکراری میباشد')

        return mobile


    def clean_national_code(self):
        national_code = self.cleaned_data.get('national_code')
        fitshow_user = FitShowUser.objects.filter(national_code=national_code).exists()
        if fitshow_user:
            raise forms.ValidationError('کد ملی وارد شده تکراری میباشد')

        return national_code




