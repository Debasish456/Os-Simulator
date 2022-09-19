from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('PS/',include('PS.urls')),
    path('BA/',include('bankers.urls')),
]
