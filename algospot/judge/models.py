from django.db import models
from django.contrib.auth.models import User

PROBLEM_STATES = {"DRAFT": 0,
        "PENDING_REVIEW": 1,
        "HIDDEN": 2,
        "PUBLISHED": 3}

class Problem(models.Model):
    key = models.CharField(max_length=64, null=False, unique=True, default="")
    name = models.CharField(max_length=128, default="")
    state = models.IntegerField(default=PROBLEM_STATES["DRAFT"],
            choices=PROBLEM_STATES.iteritems())
    author = models.ForeignKey(User, null=True, db_index=True)
    source = models.CharField(max_length=128, null=True)
    description = models.TextField(default="")
    input = models.TextField(default="")
    output = models.TextField(default="")
    sample_input = models.TextField(default="")
    sample_output = models.TextField(default="")
    note = models.TextField(default="")
    judge_module = models.CharField(max_length=128, default="")
    time_limit = models.IntegerField(default=10000)
    memory_limit = models.IntegerField(default=65536)
    accepted = models.IntegerField(default=0)
    submissions = models.IntegerField(default=0)

