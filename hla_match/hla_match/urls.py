from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Admin panel
    path('', include('donor.urls')),    # Include the URLs from the donor app
]
