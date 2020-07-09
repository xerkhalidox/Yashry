
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('user.urls')),
    path('', include('collection.urls')),
    path('', include('payment.urls')),
    path('accounts/', include('allauth.urls')),
]
