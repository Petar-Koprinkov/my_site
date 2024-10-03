from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag()
def current_time(time_string='%d-%m-%y %H:%M:%S'):
    return datetime.now().strftime(time_string)

