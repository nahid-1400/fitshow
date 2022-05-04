from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddUserForm
from .models import FitShowUser


def home(request):
    user = request.user
    return render(request, 'fitshow/home.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('users:dashboard')
            else:
                error = 'کاربر گرامی شما اجازه ورود به این پنل را ندارید'
        else:
            error = 'کاربری با این مشخصات یافت نشد'
    return render(request, 'fitshow_user/login.html', {'error': error})


@login_required(login_url='users:login')
def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required(login_url='users:login')
def add_user_view(request):
    form = AddUserForm(request.POST or None)
    if form.is_valid():
        firstname = form.cleaned_data.get('firstname')
        lastname = form.cleaned_data.get('lastname')
        fullname = f'{firstname} {lastname}'
        age = form.cleaned_data.get('age')
        mobile = form.cleaned_data.get('mobile')
        national_code = form.cleaned_data.get('national_code')
        category_course = form.cleaned_data.get('category_course')
        course_duration = form.cleaned_data.get('course_duration')
        fitshow_user = FitShowUser.objects.create(fullname=fullname, firstname=firstname, lastname=lastname, age=age,
                                                  phone=mobile, national_code=national_code,
                                                  course_duration=course_duration)
        fitshow_user.category_course.add(category_course)
        fitshow_user.course_validity_up_to_date = fitshow_user.course_validity_up_to_date_update()
        fitshow_user.save()
        return redirect('users:dashboard')
    return render(request, 'fitshow_user/add-user.html', {'form': form})


class Dashboard(LoginRequiredMixin, ListView):
    model = FitShowUser
    template_name = 'fitshow_user/dashboard.html'

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        print(query)
        if query is not None:
            return FitShowUser.objects.search(query)
        return FitShowUser.objects.all()


class UserInfo(LoginRequiredMixin, DetailView):
    model = FitShowUser
    template_name = 'fitshow_user/user-info.html'


@login_required(login_url='users:login')
def remover_user(request, user_id):
    user = get_object_or_404(FitShowUser, id=user_id)
    user.delete()
    return redirect('users:dashboard')
