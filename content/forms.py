# -*- coding: utf-8 -*-
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django import forms
from .models import Message, Order


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'text')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('created_dt', )

    def clean_attachment(self):
        attachment = self.cleaned_data['attachment']
        if attachment and attachment.size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(
                'Размер файла требований '
                'превышает максимально допустимый '
                '({})'.format(filesizeformat(settings.MAX_UPLOAD_SIZE))
            )
        return attachment
