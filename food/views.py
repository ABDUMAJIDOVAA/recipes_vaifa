from django.shortcuts import render
from .models import Category, Recipes

# Create your views here.


def all_recipes(request):
    recipes = Recipes.objects.filter(published=True)
    categories = Category.objects.all()
    context = {
        'title': "Barcha Retseptlar",
        'recipes': recipes,
        'categories': categories
    }
    return render(request, 'food/index.html', context)
