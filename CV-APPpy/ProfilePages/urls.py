from django.urls import path

from ProfilePages import views

urlpatterns = [
   
    path('profile/<str:pk>',views.profile_page, name='profile'),
    path('profiles',views.profiles, name='profiles'),

    path('profile/update/<str:pk>',views.profile_update, name='profile-update'),
    path('account/',views.account,name='account')
    
]

