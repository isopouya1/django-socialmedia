from django.contrib import admin
from django.urls import path
from core import views
app_name = 'core'
urlpatterns = [
    path('',views.home,name='home'),
    path('Signup/',views.Sign_up,name='signup')
]
