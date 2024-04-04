from django.urls import path
from .views import all_recipes

urlpatterns = [
    path('', all_recipes, name='index'),
]