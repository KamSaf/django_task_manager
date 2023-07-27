from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome_page'),
    path('todos/<str:username>/', views.TodoListView.as_view(), name='users_todos'),
    path('update/<int:pk>/', views.update_status, name='update_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('todos/<str:username>/create_todo/', views.create_todo, name='create_todo'),
    path('about/', views.about, name='about_page'),
    path('contact/', views.contact, name='contact_page')
]
