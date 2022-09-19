from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='index1'),
    path('add',views.add, name='add'),
    path('clear',views.clear, name='clear'),
    path('fcfs',views.fcfs,name="fcfs"),
    path('sjf',views.sjf,name="sjf"),
    path('rr',views.rr,name="rr"),
    path('srtf',views.srtf,name="srtf"),
    path('priority',views.priority,name="priority"),
]
