from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from .forms import AddUserForm
from .models import User





def home(request):
    user = request.user
    return render(request, 'fitshow/home.html')



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

@login_required(login_url='users:login')
def logout_view(request):
    logout(request)
    return redirect('users:login')


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
        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, age=age,
                                        phone=mobile, national_code=national_code, course_duration=course_duration)
        user.category_course.add(category_course)
        user.course_validity_up_to_date = user.course_validity_up_to_date_update()
        user.save()
        return redirect('users:dashboard')
    return render(request, 'fitshow_user/add_user.html', {'form': form})

class Dashboard(ListView):
    model = User
    template_name = 'fitshow_user/dashboard.html'


class UserInfo(DetailView):
    model = User
    template_name = 'fitshow_user/user_informations.html'

def remover_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('users:dashboard')
