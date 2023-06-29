from django.urls import path
from .views import home, pizzas, order


urlpatterns = [
    path('', home, name='home'),
    path('pizzas/', pizzas, name='pizzas'),
    path('pizzas/<int:id>/', order, name='order'),
]
