import os

from django import template

register = template.Library()


@register.filter
def getfilename(value):
    fullfilename = os.path.basename(value.file.name)
    filename = fullfilename.split('.')[0]
    return filename

def getextname(value):
    fullfilename = os.path.basename(value.file.name)
    extname = fullfilename.split('.')[-1]
    return extname
