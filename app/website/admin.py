from django.contrib import admin

# Register your models here.

from . models import Message, Minister, Category


class MessageAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Message)
admin.site.register(Minister)
admin.site.register(Category)
