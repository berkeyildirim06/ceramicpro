from django.urls import path
from . import views

urlpatterns = [
    path('api/warranties/all', views.warranty_list, name='warranty-list'),
    path('api/warranty/create/', views.warranty_create, name='warranty_create'),
    path('api/warranty/view/<int:id>', views.warranty_detail, name='warranty_detail'),
    path('api/warranty/edit/<int:id>', views.warranty_update, name='warranty_update'),
    path('api/warranty/delete/<int:pk>', views.warranty_delete, name="warranty_delete")
]