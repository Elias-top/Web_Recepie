from django import forms
from .models import Recipe, Category, RecipeCategory


class RecipeForm(forms.ModelForm):
    # categories = forms.ModelMultipleChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cooking_time', 'image', 'ingredients']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Название рецепта'  # Изменение метки
        self.fields['description'].label = 'Описание рецепта'
        self.fields['steps'].label = 'Шаги приготовления'
        self.fields['cooking_time'].label = 'Время приготовления (мин)'
        self.fields['image'].label = 'Загрузите изображение'

    # def save(self, commit=True):
    #     # Сначала вызываем родительский метод save() с commit=False.
    #     # Это сохраняет модель Recipe, но пока не сохраняет её в базу данных.
    #     instance = super().save(commit=False)
    #
    #     if commit:
    #         # Сохраняем сам объект Recipe в базу данных.
    #         instance.save()
    #
    #         # Теперь обновляем связи с категориями:
    #         # Сначала удаляем все предыдущие связи (если это редактирование рецепта).
    #         instance.recipecategory_set.all().delete()
    #
    #         # Теперь сохраняем новые связи (категории, которые пользователь выбрал в форме).
    #         for category in self.cleaned_data['categories']:
    #             # Создаём запись в таблице RecipeCategory, связывающую рецепт с категорией.
    #             RecipeCategory.objects.create(recipe=instance, category=category)
    #
    #     # Возвращаем инстанс модели Recipe (с сохранёнными данными).
    #     return instance