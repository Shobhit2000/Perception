from django.urls import path
from .views import find_user, find_all_users, signup, login, delete_user, update_user

urlpatterns = [
    path('find_user/', find_user, name='find_user'),
    path('find_all_users/', find_all_users, name='find_all_users'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('delete_user/', delete_user, name='delete_user'),
    path('update_user/', update_user, name='update_user')
]