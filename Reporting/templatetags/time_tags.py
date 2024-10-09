from django import template

register = template.Library()

@register.filter
def seconds_to_hhmm(seconds):
    """Convert seconds to hh:mm format."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours:02}:{minutes:02}"