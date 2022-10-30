from django.urls import path
from . import views


app_name = "home"

urlpatterns = [path("", views.home, name="home"),
path('thx/', views.thx, name='thx'),
]
