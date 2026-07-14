from django.contrib import admin
from .models import QuoteRequest, QuotePhoto, Gallery, GalleryPhoto


class QuotePhotoInline(admin.TabularInline):
    model = QuotePhoto
    extra = 1


@admin.register(QuoteRequest)
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
    
class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [GalleryPhotoInline]
