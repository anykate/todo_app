from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.home_page, name='index'),
    path('about/', views.about_page, name='about'),
    path('create/', views.create_todo, name='create'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete'),
]
