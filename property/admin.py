from django.contrib import admin

from .models import Flat, Claim, Owner


class FlatsOwnedInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'
    ]
    list_editable = ['new_building']
    list_filter = [
        'new_building',
        'rooms_number',
        'has_balcony',
    ]
    raw_id_fields = ['liked_by']

    inlines = [
        FlatsOwnedInline,
    ]
    exclude = ['flats_in_possession']


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'apartment']
    search_fields = ['author', 'apartment']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    list_display = ['owner_full_name', 'owner_pure_phone']
    search_fields = ['owner_full_name', 'owner_pure_phone']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
