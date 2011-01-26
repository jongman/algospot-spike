# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.inclusion_tag('pagination.html')
def paginate(p, adjacent_pages=2):
    page_numbers = [n for n in
            range(p.number - adjacent_pages,
                p.number + adjacent_pages + 1)
            if n > 0 and n <= p.paginator.num_pages]
    return {"page": p,
            "has_next": p.has_next(),
            "has_previous": p.has_previous(),
            "next": p.next_page_number(),
            "previous": p.previous_page_number()
            }
