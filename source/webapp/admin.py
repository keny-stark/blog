from django.contrib import admin
from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['description', 'status', 'text', 'created_at']


admin.site.register(Article, ArticleAdmin)
