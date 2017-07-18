# -*- coding: utf-8 -*-
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django import forms
from .models import Message, Order
import magic


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
        if attachment:
            # check type
            file_type = magic.from_buffer(attachment.read(1024), True)

            if file_type not in settings.UPLOAD_ALLOWED_MIME_TYPES:
                raise forms.ValidationError(
                    'Данный тип файла не поддерживается'
                )

            if attachment.size > settings.MAX_UPLOAD_SIZE:

                raise forms.ValidationError(
                    'Размер файла требований '
                    'превышает максимально допустимый '
                    '({})'.format(filesizeformat(settings.MAX_UPLOAD_SIZE))
                )
        return attachment
