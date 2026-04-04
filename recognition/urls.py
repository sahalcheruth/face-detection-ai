

from django.urls import path
from .views import upload_images, scan_face

urlpatterns = [
    path('upload-images/', upload_images),
    path('scan-face/', scan_face),
]