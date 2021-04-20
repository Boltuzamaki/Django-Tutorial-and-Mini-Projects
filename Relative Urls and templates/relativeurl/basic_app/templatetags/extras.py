from django import template

register = template.Library()

def cut(value,arg):
    """
    This cuts out whole value of arg from string!
    """
    return value.replace(arg, '')

register.filter('cut', cut)
