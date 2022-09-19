from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('process/',include('PS.urls')),
    path('',include('homepage.urls')),
    path('banker/',include('bankers.urls')),
]
