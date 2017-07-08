# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (ExtraBlock, MenuItem, UnruledNumbers,
                     Client, WhyUnruled, Portfolio, PortfolioImage)


@admin.register(ExtraBlock)
class ExtraBlockAdmin(admin.ModelAdmin):

    list_display = ('name', 'is_active')
    list_filter = ('is_active',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('title',)


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
