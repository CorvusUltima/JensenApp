from django.urls import path
from django.contrib import admin
from MainPages import views

urlpatterns = [
   
     path('', views.home, name='home'),
    
    path('login/',views.login_page, name='login'),

    path('logout/', views.logout_page, name='logout'),

    path('register/',views.register_page, name='register'),

    path('admin/', admin.site.urls , name='admin'),

    
]

