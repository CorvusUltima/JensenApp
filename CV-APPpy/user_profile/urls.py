from django.urls import path

from user_profile import views

urlpatterns = [
   
    path('',views.profile_page, name='profile'),
   
]

