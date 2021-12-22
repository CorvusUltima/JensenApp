from django.urls import path

from user_profile import views

urlpatterns = [
   
    path('',views.profile_page, name='profile'),
    path('profiles',views.profiles, name='profiles'),
    path('update/',views.profile_update, name='profile-update'),
    path('test/',views.test, name='test')
]

