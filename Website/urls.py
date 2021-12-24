from django.urls import path
from Website.views import home

app_name = 'Website'

urlpatterns = [
    
    path('', home.show, name='home'),

]