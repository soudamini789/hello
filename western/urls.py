from django.urls import path
from western.views import *
app_name='mini'
urlpatterns=[
    path('nini/',gowns,name='gowns'),#gowns/=suffixname,gowns=functionaddress,'gowns=urlmap name
]