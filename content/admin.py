# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (ExtraBlock, MenuItem, UnruledNumbers,
                     Client, WhyUnruled, Portfolio, PortfolioImage,
                     Message, Order)
from mptt.admin import MPTTModelAdmin
from adminsortable2.admin import SortableAdminMixin


@admin.register(ExtraBlock)
class ExtraBlockAdmin(admin.ModelAdmin):

    list_display = ('name', 'is_active')
    list_filter = ('is_active',)


@admin.register(MenuItem)
class MenuItemAdmin(SortableAdminMixin, MPTTModelAdmin):

    ordering = ('order', )
    list_display = ('title', 'position')
    list_filter = ('position', )


@admin.register(UnruledNumbers)
class UnruledNumbersAdmin(admin.ModelAdmin):
    list_display = ('number', 'measure_unit')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(WhyUnruled)
class WhyUnruledAdmin(admin.ModelAdmin):
    list_display = ('text', )


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 0


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'release_date')
    inlines = (PortfolioImageInline, )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_dt')
    readonly_fields = ('created_dt', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_or_email', 'created_dt')
    readonly_fields = ('created_dt', )
