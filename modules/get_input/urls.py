from django.urls import path

from . import views

app_name = 'get_input'

urlpatterns = [
    path( '',         views.index,    name='get_input' ),
    path( 'response', views.response, name='response'  ),
]
