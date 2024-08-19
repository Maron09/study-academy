from django import template

register = template.Library()


@register.filter
def format_duration(value):
    if value < 3600:  # Less than an hour
        if value <= 60:  # Less than or equal to 60 minutes
            return f"{value:.0f} Minutes"  # Convert seconds to minutes
        else:
            return f"{value / 3600:.0f} Hours"  # Convert seconds to hours
    else:  # More than an hour
        return f"{value / 3600:.0f} hours" 


@register.filter
def to_range(value, arg):
    return range(value, arg + 1)


@register.filter
def subtract(value, arg):
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return ''