from django.urls import path
from ethnic.views import *
app_name='mini'
urlpatterns=[
    path('anarkali/',anarkali,name='anarkali'),
]