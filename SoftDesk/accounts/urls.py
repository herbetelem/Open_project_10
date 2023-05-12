from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signup/', views.register_view, name='register_view'),
    path('profil/<id>/', views.profile_page, name='profile_page'),
]

