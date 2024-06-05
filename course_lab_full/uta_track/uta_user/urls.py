"""
URL configuration for uta_track project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('user_edit/',views.UserCreateEdit.as_view(),name='user_create_edit'),
    path('my_routes_list/',views.RouteListView.as_view(),name='my_routes_list'),
    path('route_map/',views.RouteMapView.as_view(),name='route_map'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('faq/',views.FaqView.as_view(),name='faq'),
    path('comment_list/',views.CommentList.as_view(),name='comment_list'),
]

