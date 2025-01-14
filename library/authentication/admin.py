from django.contrib import admin
from .models import CustomUser, AuthorProxy, BookProxy, OrderProxy

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(AuthorProxy)
class AuthorProxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    search_fields = ('name', 'surname', 'patronymic')
    list_filter = ('name', 'surname', 'patronymic')

@admin.register(OrderProxy)
class OrderProxyAdmin(admin.ModelAdmin):

    def book_name(self, obj):
        return obj.book.name
    book_name.short_description = 'Book'

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User'

    list_display = ('id', 'book_name', 'user_email', 'created_at', 'end_at', 'plated_end_at')
    search_fields = ('user', 'book_name', 'created_at', 'end_at', 'plated_end_at')
    list_filter = ('book', 'user', 'created_at', 'end_at', 'plated_end_at')


@admin.register(BookProxy)
class BookProxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count', 'year_of_publication', 'get_authors')
    search_fields = ('name', 'description', 'year_of_publication', 'authors__name', 'authors__surname', 'authors__patronymic')
    list_filter = ('count', 'name', 'description', 'year_of_publication')

    def get_authors(self, obj):
        return ", ".join([f"{author.name} {author.surname} {author.patronymic}" for author in obj.authors.all()])
    get_authors.short_description = 'Authors'