from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.owner_home, name='home'),
    path('hello/', views.helloworld, name='helloworld'),
    path('polls/owner',views.owner_home, name='owner_home'),
    path('hello/hello/', views.hello, name='helloworld_2'),
]
