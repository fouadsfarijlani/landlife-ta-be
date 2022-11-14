from django.urls import path
from lovely_trees_api import views

urlpatterns = [
    path('', views.get_data),
    path('add/', views.addData),
]