# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ExtraBlock, MenuItem


@admin.register(ExtraBlock)
class ExtraBlockAdmin(admin.ModelAdmin):

    list_display = ('name', 'is_active')
    list_filter = ('is_active',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('title',)
