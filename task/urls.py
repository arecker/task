from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('password-reset/', views.PasswordReset.as_view(), name='password-reset'),
    path('password-reset/done/', views.PasswordResetDone.as_view(), name='password-reset-done'),
    path('password-reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password-reset-confirm'),
    path('password-reset/complete/', views.PasswordResetComplete.as_view(), name='password-reset-complete'),
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/new/', views.TaskCreate.as_view(), name='task-create')
]
