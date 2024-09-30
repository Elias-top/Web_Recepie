from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import RecipeForm
from .models import Recipe, RecipeCategory, Category
import random

def index(request):
    recipes = Recipe.objects.all().order_by('?')[:5]
    return render(request, 'index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            # Сохраняем связи с категориями
            selected_categories = request.POST.getlist('categories')  # Получаем выбранные категории из POST-запроса
            for category_id in selected_categories:
                category = Category.objects.get(id=category_id)
                RecipeCategory.objects.create(recipe=recipe, category=category)  # Создаем связь между рецептом и категорией

            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    categories = Category.objects.all()  # Получаем все категории
    return render(request, 'add_recipe.html', {'form': form, 'categories': categories})

def get_my_recipes(request):
    recipes = Recipe.objects.filter(author = request.user).order_by('title')
    return render(request, 'get_my_recepie.html', {'recipes': recipes})
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()

            # Удаляем старые связи и создаем новые
            RecipeCategory.objects.filter(recipe=recipe).delete()  # Удаляем старые категории
            selected_categories = request.POST.getlist('categories')  # Получаем выбранные категории
            for category_id in selected_categories:
                category = Category.objects.get(id=category_id)
                RecipeCategory.objects.create(recipe=recipe, category=category)  # Создаем связь между рецептом и категорией
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    categories = Category.objects.all()  # Получаем все категории
    selected_categories = recipe.recipecategory_set.values_list('category_id', flat=True)  # Получаем связанные категории

    return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe, 'categories': categories,
                                                'selected_categories': selected_categories})

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'  # Шаблон для регистрации
    success_url = reverse_lazy('login')