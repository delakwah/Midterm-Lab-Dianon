from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import ReportView, ItemsView, DetailView, DeleteView, UpdateView, home

urlpatterns = [
    path('', home, name='index'),
    path('items/', ItemsView.as_view(), name='items'),
    path('report/', ReportView.as_view(), name='report'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update'),
    path('claim/<int:item_id>/', views.claim_item, name='claim'),
    path('login/', views.login_view, name='login'),
    path('register/', views.signup_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profiles/', views.profile_view, name='profiles'),
]