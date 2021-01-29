from django.urls import path

from catalog import views as catalog_views
from . import views

urlpatterns = [
    path('client/create/', views.ClientCreate.as_view(), name='client-create'),
    path('client/<int:pk>/update/', views.ClientUpdate.as_view(), name='client-update'),
    path('client/<int:pk>/delete/', views.ClientDelete.as_view(), name='client-delete'),
    path('', views.ClientListView.as_view(), name='client-list'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name= 'client-details')
]
