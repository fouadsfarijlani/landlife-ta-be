from django.urls import path
from lovely_trees_api import views

urlpatterns = [
    path('', views.get_data),
    path('add/', views.addData),
    path('uploadSpeciesDataFile/', views.UploadSpeciesFileView.as_view(), name='upload-species-file'),
    path('uploadFieldDataFile/', views.UploadFieldDataFileView.as_view(), name='upload-filed-data-file')
]