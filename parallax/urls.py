from django.urls import path

from parallax import views

urlpatterns = [
    path('direction/', views.direction),
    path('direction/update/', views.direction_update),
]