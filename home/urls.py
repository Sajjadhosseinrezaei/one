from django.urls import path
from . import views
urlpatterns = [
    path('sajjad/', views.sajjad, name = 'sajjad'),
    path('',views.home, name='home'),
    path('detail/<int:todo_id>/', views.detail , name='detail'),
    path('person_detail/<int:pd>/', views.pdetail, name='person_details'),
    path('delete/<int:todo_id>/', views.delete, name = 'delete_object'),
    path('delete_person/<int:pd>/', views.pdelete, name = 'pdelete'),
    path('create/', views.create, name='create'),
    path('update/<int:todo_id>',views.update, name='update'),
]