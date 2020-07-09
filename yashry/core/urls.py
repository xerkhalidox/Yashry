from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pages/men', views.pagetype_template, name="menpage"),
    path('pages/women', views.pagetype_template, name="womenpage"),
    path('pages/kids', views.pagetype_template, name="kidspage"),

]
