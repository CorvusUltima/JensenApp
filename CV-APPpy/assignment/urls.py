from django.urls import path

from assignment import views

urlpatterns = [
    path('',views.home,name='home'),
    path('assignment/', views.index, name='all-assignments'),
    path('assignment/success',views.registration_confirmation, name ='confirm-registration'),
    path('assignment/<slug:assignment_slug>', views.assignment_details, name='assignment-details'),

]

