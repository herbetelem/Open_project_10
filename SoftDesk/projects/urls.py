from django.urls import path
from . import views

urlpatterns = [
    # Global
    path('', views.home_page, name='home_page'),
]
