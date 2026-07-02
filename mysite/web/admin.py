from django.contrib import admin
from .models import Customer, QuotePhoto


class QuotePhotoInline(admin.TabularInline):
    model = QuotePhoto
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone",
        "email",
        "project_type",
        "budget",
        "created_at",
    )
    search_fields = (
        "full_name",
        "email",
        "phone",
    )
    list_filter = (
        "project_type",
        "budget",
        "timeline",
    )
    inlines = [QuotePhotoInline]