from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import AddUserForm
from .models import User

def home(request):
    user = request.user
    return render(request, 'fitshow_user/home.html')



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'کاربری با این مشخصات پیدا نشد لطفا از صحت اطلاعات وارد شده اطمنیان حاصل گردانید'
    return render(request, 'fitshow_user/login_dashboard.html', {'error': error})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


def add_user_view(request):
    form = AddUserForm(request.POST or None)
    if form.is_valid():
        firstname = form.cleaned_data.get('firstname')
        lastname = form.cleaned_data.get('lastname')
        username = f'{firstname} {lastname}'
        age = form.cleaned_data.get('age')
        mobile = form.cleaned_data.get('mobile')
        national_code = form.cleaned_data.get('national_code')
        category_course = form.cleaned_data.get('category_course')
        course_duration = form.cleaned_data.get('course_duration')
        user = User.objects.create_user(username= username, first_name=firstname, last_name=lastname, age=age, phone=mobile, national_code=national_code, course_duration=course_duration)
        user.category_course.add(category_course)
        user.save()
        return redirect('home')
    return render(request, 'fitshow_user/add_user.html', {'form': form})


