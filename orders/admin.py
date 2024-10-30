from django.contrib import admin

from orders.models import Order, User, Cryptocurrency


# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'cryptocurrency', 'amount', 'processed')
    list_filter = ('cryptocurrency', 'user')
    show_facets = admin.ShowFacets.ALWAYS
    ordering = ('cryptocurrency',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'balance')
    list_filter = ('username',)
    show_facets = admin.ShowFacets.ALWAYS
    ordering = ('username',)


@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('name',)
    show_facets = admin.ShowFacets.ALWAYS
    ordering = ('name',)
