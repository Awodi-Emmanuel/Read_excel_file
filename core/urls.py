from django.urls import path
from core import views


urlpatterns = [
    path('', views.test, name='test'),
    
]
