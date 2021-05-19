# from django.contrib import admin
from django.contrib.admin import ModelAdmin, site
from chat.models import MessageModel


class MessageModelAdmin(ModelAdmin):
    readonly_fields = ('timestamp',)
    search_fields = ('id', 'body', 'user__username', 'recipient__username')
    list_display = ('id', 'user', 'recipient', 'timestamp', 'characters')
    list_display_links = ('id',)
    list_filter = ('user', 'recipient')
    date_hierarchy = 'timestamp'


site.register(MessageModel, MessageModelAdmin)

# Register your models here.
