from django import template
import math

register = template.Library()
@register.filter

def time_formatter(time):
    time = int(time)
    seconds = math.floor( time % 60)
    minutes = math.floor((time % 3600) / 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    return f"{minutes}:{seconds}"
