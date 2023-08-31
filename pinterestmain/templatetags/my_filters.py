from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def compact_naturaltime(value):
    now = timezone.now()
    if value > now:
        delta = value - now
        delta_seconds = delta.total_seconds()
        if delta_seconds < 60:
            return f"{int(delta_seconds)}s"
        elif delta_seconds < 3600:
            return f"{int(delta_seconds / 60)}m"
        elif delta_seconds < 86400:
            return f"{int(delta_seconds / 3600)}h"
        else:
            return f"{int(delta_seconds / 86400)}d"
    else:
        delta = now - value
        delta_seconds = delta.total_seconds()
        if delta_seconds < 60:
            return f"{int(delta_seconds)}s"
        elif delta_seconds < 3600:
            return f"{int(delta_seconds / 60)}m"
        elif delta_seconds < 86400:
            return f"{int(delta_seconds / 3600)}h"
        else:
            return f"{int(delta_seconds / 86400)}d"

@register.filter
def remove_https(value):
    print(f"remove_http called with value: {value}")
    return value.replace('http://', '')