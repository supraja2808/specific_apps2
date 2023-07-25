from django.urls import path
from app2.views import *

urlpatterns=[
    path('h3/',h3,name='h3'),
    path('h4/',h4,name='h4'),
]