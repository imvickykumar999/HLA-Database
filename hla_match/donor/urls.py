from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_donor, name='register_donor'),  # URL to register donors
    path('', views.match_donor, name='match_donor'),           # URL to search for HLA matches
]
