from django.urls import path
from .views import login_view, logout_view, add_user_view, Dashboard, UserInfo, remover_user

app_name = 'users'

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('add_user', add_user_view, name='add-user'),
    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('user_info/<pk>', UserInfo.as_view(), name='user-info'),
    path('remove_user/<user_id>', remover_user, name='remove-user'),
]
