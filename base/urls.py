from unicodedata import name
from django.urls import path
from .views import home, delete_account,room, topicsPage ,update_user ,create_room, update_room, delete_room, login_user, logout_user, register_user, delete_message, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('room/<str:pk>/', room, name='room'),
    path('create-room/', create_room, name='create-room'),
    path('update-room/<str:pk>', update_room, name='update-room'),
    path('delete-room/<str:pk>', delete_room, name='delete-room'),
    path('delete-message/<str:pk>', delete_message, name='delete-message'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('delete/', delete_account, name='delete_account' ),
    path('profile/<str:pk>', profile, name='profile'),
    path('update-user/', update_user, name='update-user'),
    path('topics/', topicsPage, name='topics'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='base/reset_password.html'), name='reset_password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='base/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='base/reset_password_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='base/reset_password_done.html'), name='password_reset_complete'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='base/change_password.html'), name='change_password'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='base/change_password_done.html'), name='password_change_done'),
]