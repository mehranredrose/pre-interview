from django.urls import path
from . import views

urlpatterns = [
    path('addphone',views.add_phone),
    path('report/', views.report),
    
]