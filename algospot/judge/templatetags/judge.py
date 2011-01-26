# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.simple_tag
def ac_ratio(problem):
    if problem.submissions == 0:
        return "0 (0)"
    return "%.2lf%% (%d)" % (problem.accepted * 100.0 / problem.submissions,
            problem.accepted)
