from django.contrib import admin

# Register your models here.
from .models import Statement, Response


class StatementAdmin(admin.ModelAdmin):
    list_display = ('text', )
    list_filter = ('text', )
    search_fields = ('text', )


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('statement', 'response', )
    search_fields = ['statement__text', 'response']

admin.site.register(Statement, StatementAdmin)
admin.site.register(Response, ResponseAdmin)
