from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('my_recipes/', views.get_my_recipes, name='get_my_recipes'),
    path('recipe/edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),

    path('register/', RegisterView.as_view(), name='register'),  # Страница регистрации
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Страница входа
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Страница выхода
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)