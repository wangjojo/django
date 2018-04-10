from django.contrib import admin
from .models import *
# Register your models here.

class CategroyAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','categroy','content','pub')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog','name','content','pub')

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Categroy,CategroyAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Comment,CommentAdmin)