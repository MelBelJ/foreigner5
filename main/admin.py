from django.contrib import admin
from .models import Casas, Blogs

class CasasAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class BlogsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Casas, CasasAdmin)
admin.site.register(Blogs, BlogsAdmin)
# Register your models here.
