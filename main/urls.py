from main import views
from django.urls import path, include

urlpatterns = [    
    path('', views.index, name='index'),
    path('submit-list/', views.submitList, name='submit-list'),
    path('delete-list/<int:id>/', views.deleteList, name='delete-list'),
    path('edit-list;<int:id>/', views.editList, name='edit-list'),
]
