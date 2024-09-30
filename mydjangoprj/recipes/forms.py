from django import forms
from .models import Recipe
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        #fields = ['title', 'description', 'steps', 'cooking_time', 'image', 'ingredients']
        fields = ['title', 'description', 'steps', 'cooking_time', 'image', 'ingredients']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Название рецепта'  # Изменение метки
        self.fields['description'].label = 'Описание рецепта'
        self.fields['steps'].label = 'Шаги приготовления'
        self.fields['cooking_time'].label = 'Время приготовления (мин)'
        self.fields['image'].label = 'Загрузите изображение'