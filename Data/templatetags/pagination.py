from django import template
import urllib

register = template.Library()

@register.simple_tag(takes_context=True)
def get_custum_pagination(context,page_no, current):
    """pagination"""
    cls = """ class="active" """
    r = range(0, 2)
    text = """<li {}> <a href="?page={}&%s">{}</a> </li>""".format('{}', current,current)
    if (page_no - current in r) or (current - page_no in r):
        if page_no == current:
            text = text.format(cls)
        else:
            text = text.format('')
        text = text %(urllib.urlencode(context.get('query_items','')))
        return text
    else:
        return ''
