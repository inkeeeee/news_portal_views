from django import template
from .badwords import BADWORDS

register = template.Library()


@register.filter()
def censor(value):
    if type(value) != str:
        raise TypeError

    for word in BADWORDS:
        value = value.replace(word, word[0] + '*' * (len(word) - 1))
        value = value.replace(word.capitalize(), word[0].upper() + '*' * (len(word) - 1))

    return value
