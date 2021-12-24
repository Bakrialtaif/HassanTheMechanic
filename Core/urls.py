from django.urls import path
from Core.views import home

app_name = 'Core'

urlpatterns = [
    
    path('', home.show, name='core-home'),

]