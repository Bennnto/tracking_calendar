from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_expense, name='expense'),
    path('create/', views.create_expense, name='create_expense'),
    path('del/<int:id>', views.delete_expense, name='delete_expense')
]