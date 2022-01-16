"""
Definition of urls for CV_APPpy.
"""

from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('ProfilePages.urls')),
     path('', include('MainPages.urls'))
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
