from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('trigger-websocket/', views.trigger_websocket, name='trigger_websocket'),
    # path('', views.HomePageView.as_view(), name='home'),
]
