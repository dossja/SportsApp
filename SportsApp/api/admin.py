from django.contrib import admin
from .models import CommentModel, PostModel, ImageModel

# Register your models here.
@admin.register(PostModel.Post)
class PostAdmin(admin.ModelAdmin):
    """Admin for Post."""


@admin.register(CommentModel.Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin for Comments."""


@admin.register(ImageModel.Image)
class ImageAdmin(admin.ModelAdmin):
    """Admin for Images."""
