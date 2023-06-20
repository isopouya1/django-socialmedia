from django.contrib import admin
from django.urls import path
from core import views
app_name = 'core'
urlpatterns = [
    path('',views.home,name='home'),
    path('Signup/',views.Sign_up,name='signup'),
    path('Signin/',views.signin,name='signin'),
    path('logout/',views.logout,name='logout'),
    path('setting/',views.setting,name='setting'),
    path('upload/',views.upload,name='upload'),
    path('profile/<str:username>',views.profile,name='profile'),
    path('like-post/<post_id>',views.like,name="like"),
    path('comment/',views.comment,name='comment'),
    path('delete/<post_id>',views.delete,name='delete'),
    path('del/<comment_slug>',views.dlcm,name='delcm'),
    path('search', views.search, name='search'),
]
