# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
    path('solicitudes/crear/', views.crear_solicitud, name='crear_solicitud'),
    path('solicitudes/<int:id>/', views.detalle_solicitud, name='detalle_solicitud'),
]