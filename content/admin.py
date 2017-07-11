# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (ExtraBlock, MenuItem, UnruledNumbers,
                     Client, WhyUnruled, Portfolio, PortfolioImage,
                     Message, Order)
from mptt.admin import MPTTModelAdmin


@admin.register(ExtraBlock)
class ExtraBlockAdmin(admin.ModelAdmin):

    list_display = ('name', 'is_active')
    list_filter = ('is_active',)


@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):

    list_display = ('title', 'position')
    list_filter = ('position', )


@admin.register(UnruledNumbers)
class UnruledNumbersAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(WhyUnruled)
class WhyUnruledAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass


@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_or_email', 'created_dt')
    readonly_fields = ('created_dt', )
