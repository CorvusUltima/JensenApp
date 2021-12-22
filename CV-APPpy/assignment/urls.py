from django.urls import path

from assignment import views

urlpatterns = [
   
    path('assignment/', views.index, name='all-assignments'),
    path('assignment/success',views.registration_confirmation, name ='confirm-registration'),
    path('assignment/create-assignment',views.create_assignment, name='create-assignment'),

    path('assignment/<str:pk>', views.assignment_details, name='assignment-details'),

    path('assignment/<str:pk>/applicant-form',views.apply, name='applicant-form'),

     

]

