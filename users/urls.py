from django.urls import path, include
from .views import register, logout


urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
