from django.contrib import admin
from link_aggregator.core.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["url", "description"]
