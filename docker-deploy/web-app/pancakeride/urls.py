from django.urls import path, re_path
from django.views.generic.base import TemplateView 
from .import views

app_name = 'pancakeride'
urlpatterns =[
    path('driver/register/', views.Driver_regist, name='driver_register'),
    #path('ride/on-going/'),
    re_path(r'^ride/list/$', views.RideListView.as_view(), name = 'ride_list'),
    #path('ride/history/', views.RideListView.as_view(), name = 'history_ride'),
    path('ride/request/', views.Ride_request, name='ride_request'),
    path('ride/edit/<uuid:pk>/', views.Ride_request_edit, name='ride_request_edit'),
    path('ride/detail/<uuid:pk>/', views.Ride_request_detail, name='ride_detail'),
    path('home/', TemplateView.as_view(template_name='Home/main_home.html'), name='main_home'),
    re_path(r'^sharer/search/$', views.Sharer_search, name='sharer_search'),
    path('sharer/confirm/<uuid:pk>/', views.Sharer_confirm, name='sharer_confirm'),
    path('driver/search/', views.Driver_search, name='driver_search'),
    path('driver/confirm/<uuid:pk>/', views.Driver_confirm, name='driver_confirm'),
    path('driver/complete/<uuid:pk>', views.Driver_complete, name='driver_complete'),
    #path('home/', )
]