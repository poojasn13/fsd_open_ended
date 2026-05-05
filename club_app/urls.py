from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_event/', views.add_event, name='add_event'),
    path('view_events/', views.view_events, name='view_events'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('view_volunteers/', views.view_volunteers, name='view_volunteers'),
]