from django.contrib import admin
from .models import CEO, Blog


class CEOAdmin(admin.ModelAdmin):
    model = CEO
    list_display = ('name', 'corparation', 'annotation', 'date_create', 'moneys', 'id')

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ('author', 'text','date_create')

admin.site.register(CEO, CEOAdmin)
admin.site.register(Blog, BlogAdmin)
