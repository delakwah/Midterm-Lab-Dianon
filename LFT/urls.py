from django.urls import path
from . import views
from .views import delete, update

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('report/', views.report, name='report'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
]