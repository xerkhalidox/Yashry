from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.Login.as_view(), name="login"),
    path('accounts/signup/', views.register, name="signup"),
]
