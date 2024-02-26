from django.urls import path 
from django.contrib import admin
from . import views 
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('candidates',views.all_candidates)

urlpatterns =[
    path ('candidates/' ,views.all_candidate),
    path ('categories/', views.all_categories)
]