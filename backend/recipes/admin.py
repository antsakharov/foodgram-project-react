from django.contrib import admin
from collections import Count
from foodgram.settings import EMPTY
from .models import Favorite, Ingredient, Recipe, ShoppingCart, Tag


class IngredientsInLine(admin.TabularInline):
    model = Recipe.ingredients.through


class TagsInLine(admin.TabularInline):
    model = Recipe.tags.through


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'recipe']
    search_fields = ['user__username', 'user__email']
    empty_value_display = EMPTY


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'measurement_unit']
    search_fields = ['name']
    empty_value_display = EMPTY


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'favorites']
    search_fields = ['name', 'author__username']
    list_filter = ['tags']
    empty_value_display = EMPTY
    inlines = (
        IngredientsInLine, TagsInLine
    )

    def favorites(self, obj):
        fav_objects = Favorite.objects.filter(recipe=obj)
        return fav_objects.aggregate(count=Count('id'))['count'] or 0


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'recipe']
    search_fields = ['user__username', 'user__email']
    empty_value_display = EMPTY


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color', 'slug']
    search_fields = ['name', 'slug']
    empty_value_display = EMPTY
