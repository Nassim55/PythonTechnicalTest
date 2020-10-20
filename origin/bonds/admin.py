from django.contrib import admin
from bonds.models import Bond

class BondAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'isin', 'size', 'currency', 'maturity', 'lei')
    search_fields = ('id', 'user', 'isin', 'size', 'currency', 'maturity', 'lei')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Bond, BondAdmin)