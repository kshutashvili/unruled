# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BotPerson, BotQuestion, BotAnswer, UserAnswer


@admin.register(BotPerson)
class BotPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'greeting')


class BotAnswerInline(admin.TabularInline):
    model = BotAnswer
    extra = 0


@admin.register(BotQuestion)
class BotQuestionAdmin(admin.ModelAdmin):
    list_display = ('person', 'title')
    inlines = (BotAnswerInline, )


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'name', 'email', 'created_dt')
    readonly_fields = ('created_dt',)
