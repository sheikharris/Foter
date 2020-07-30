from django.urls import path
from . import views

urlpatterns = [
    path('owner', views.owner,name="owner"),
    path('app',views.app,name="app"),
    path('watercos',views.watercos,name="watercos"),



]
