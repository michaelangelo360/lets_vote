from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from django.contrib import admin
from . import views 
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('candidates',views.all_candidates)

urlpatterns =[
    path ('candidates/' ,views.all_candidate),
    path ('categories/', views.all_categories),
    path ('nominees/' , views.all_nominees)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)