from django.urls import path
from django.conf.urls import url
from registion import views

app_name = 'register'
urlpatterns = [
  path('register/', views.RegisterView.as_view(), name='register'),
]