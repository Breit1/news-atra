from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def bold_stars(value):
    # Заменяем звездочку перед словом на жирный текст слова
    value = re.sub(r'\*(\w+)', r'<strong>\1</strong>', value)
    # Заменяем звездочку перед одинарными кавычками на жирный текст внутри кавычек
    value = re.sub(r'\*\'([^\']+)\'', r'<strong>\'\1\'</strong>', value)
    # Заменяем звездочку перед двойными кавычками на жирный текст внутри кавычек
    value = re.sub(r'\*\"([^\"]+)\"', r'<strong>"\1"</strong>', value)
    # Заменяем звездочку перед символом « на жирный текст внутри кавычек
    value = re.sub(r'\*(«[^»]+»)', r'<strong>\1</strong>', value)
    
    return mark_safe(value)


