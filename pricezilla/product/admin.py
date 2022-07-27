from django.contrib import admin
from .models import Product, Store, Category, Comment

admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Comment)

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cotent', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)