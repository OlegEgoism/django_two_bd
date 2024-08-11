from django.contrib import admin

from two.models import TwoInfo


@admin.register(TwoInfo)
class TwoInfoAdmin(admin.ModelAdmin):
    """Вторая БД запись"""
    list_display = 'name',
    search_fields = 'name',
    search_help_text = 'Поиск'
    list_per_page = 20
