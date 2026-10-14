from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply value by argument."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def currency(value):
    """Format a number as currency."""
    try:
        return f"${float(value):,.2f}"
    except (ValueError, TypeError):
        return "$0.00"
