from django.db import models

PROBLEM_STATES = {"DRAFT": 0,
        "PENDING_REVIEW": 1,
        "HIDDEN": 2,
        "PUBLISHED": 3}

class Problem(models.Model):
    name = models.CharField(max_length=128, default="")
    description = models.TextField(default="")
    state = models.IntegerField(default=PROBLEM_STATES["DRAFT"],
            choices=PROBLEM_STATES.iteritems())
