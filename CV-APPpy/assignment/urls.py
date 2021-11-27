from django.urls import path

from assignment import views

urlpatterns = [
   
    path('assignment/', views.index, name='all-assignments'),
    path('assignment/applicant-form',views.form, name='form'),
    path('assignment/success',views.registration_confirmation, name ='confirm-registration'),
    path('assignment/<slug:assignment_slug>', views.assignment_details, name='assignment-details'),

]

