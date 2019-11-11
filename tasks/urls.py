from django.urls import path
from . import views

urlpatterns = (
    path('', views.listIndex, name='index-list'),
    path('dashboard/', views.dashboard, name='dashboard'),
)

