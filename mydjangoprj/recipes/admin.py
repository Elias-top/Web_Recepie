from django.contrib import admin

from recipes.models import Recipe, Category, RecipeCategory

admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(RecipeCategory)
# Register your models here.
