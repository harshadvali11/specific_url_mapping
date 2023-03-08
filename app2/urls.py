from app2.views import *

from django.urls import path

app_name='nothing'

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('abd/',abd,name='abd'),
]