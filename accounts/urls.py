from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('loggin', views.loggin_form, name='loggin'),
    path('logout',views.logout_form,name='logout'),
]