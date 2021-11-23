from django.contrib import admin
from .models import Image, Comment

class ImageAdmin(admin.ModelAdmin):
    fields = ['title', 'pub_date', 'url']

admin.site.register(Image, ImageAdmin)
admin.site.register(Comment)