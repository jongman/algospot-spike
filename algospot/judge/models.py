from django.db import models

PROBLEM_STATES = {"DRAFT": 0,
        "PENDING_REVIEW": 1,
        "HIDDEN": 2,
        "PUBLISHED": 3}

class Problem(models.Model):
    Name = models.CharField(max_length=128)
    Description = models.TextField()
    State = models.IntegerField(default=0, choices=PROBLEM_STATES.iteritems())
