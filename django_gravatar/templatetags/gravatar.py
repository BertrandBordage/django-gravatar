from django import template
from django.utils.html import escape

from django_gravatar.helpers import get_gravatar_url, has_gravatar as has_gravatar_helper, GRAVATAR_DEFAULT_SIZE

# Get template.Library instance
register = template.Library()


@register.filter
def has_gravatar(user_or_email):
    return has_gravatar_helper(user_or_email)


@register.simple_tag
def gravatar_url(user_or_email, size=GRAVATAR_DEFAULT_SIZE):
    """ Builds a gravatar url from an user or email """
    if hasattr(user_or_email, 'email'):
        email = user_or_email.email
    else:
        email = user_or_email

    try:
        return escape(get_gravatar_url(email=email, size=size))
    except:
        return ''


@register.simple_tag
def gravatar(user_or_email, size=GRAVATAR_DEFAULT_SIZE, alt_text='', css_class='gravatar'):
    """ Builds an gravatar <img> tag from an user or email """
    if hasattr(user_or_email, 'email'):
        email = user_or_email.email
    else:
        email = user_or_email

    try:
        url = escape(get_gravatar_url(email=email, size=size))
    except:
        return ''

    return '<img class="{css_class}" src="{src}" width="{width}" height="{height}" alt="{alt}" />'.format(\
        css_class=css_class, src=url, width=size, height=size, alt=alt_text)
