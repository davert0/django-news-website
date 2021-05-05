from django.contrib import admin

from .models import News, Category


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'published_at', 'updated_at', 'published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('published',)
    list_filter = ('published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
