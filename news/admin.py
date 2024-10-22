from django.contrib import admin
from .models import News_post

# Регистрация модели News_post для админки
@admin.register(News_post)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author')
    search_fields = ('title', 'short_description')
    list_filter = ('pub_date', 'author')
