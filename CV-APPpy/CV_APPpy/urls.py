"""
Definition of urls for CV_APPpy.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    path('login/',views.login_page, name='login'),

    path('logout/', views.logout_page, name='logout'),

    path('register/',views.register_page, name='register'),

    path('admin/', admin.site.urls),
    
    path('', include('assignment.urls')),

    path('profile/', include('user_profile.urls')),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
