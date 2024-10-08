from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.IntegerField(help_text="Время приготовления в минутах")
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('recipe', 'category')