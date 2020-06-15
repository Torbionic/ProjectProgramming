from django.contrib import admin
from .models import CEO


class CEOAdmin(admin.ModelAdmin):
    model = CEO
    list_display = ('name', 'corparation', 'annotation', 'date_create', 'moneys', 'id')


admin.site.register(CEO, CEOAdmin)

