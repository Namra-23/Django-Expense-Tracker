from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login,name='login'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
]