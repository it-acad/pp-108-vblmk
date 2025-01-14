from django.contrib import admin
from .models import CustomUser, AuthorProxy, BookProxy

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(AuthorProxy)
class AuthorProxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')
    search_fields = ('name', 'surname')

@admin.register(BookProxy)
class BookProxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count')
    search_fields = ('name',)