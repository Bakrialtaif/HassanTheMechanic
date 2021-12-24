from django import template
from django.contrib.messages import get_messages

from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag('tags/messages_bar.html', takes_context=True)
def messages_bar(context):
    return {
        'messages': get_messages(context['request']),
        }

@register.inclusion_tag('tags/website_footer.html', takes_context=True)
def website_footer(context):
    return {
        'request': context['request'],
    }
