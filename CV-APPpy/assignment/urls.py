from django.urls import path

from assignment import views

urlpatterns = [
    path('assignment/', views.index, name="all-assignments"),
    path('assignment/<slug:assignment_slug>', views.assignment_details, name='assignment-details'),

]

