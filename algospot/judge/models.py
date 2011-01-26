from django.db import models
from django.contrib.auth.models import User

PROBLEM_STATES = {"DRAFT": 0,
        "PENDING_REVIEW": 1,
        "HIDDEN": 2,
        "PUBLISHED": 3}

class Problem(models.Model):
    key = models.CharField(max_length=64, unique=True, default="")
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
    updated = models.DateTimeField(null=True, auto_now=True, db_index=True)

    def __unicode__(self):
        return "%s (%s)" % (self.key, self.name)

SUBMISSION_STATES = {"RECEIVED": 0,
        "COMPILING": 1,
        "RUNNING": 2,
        "JUDGING": 3,
        "COMPILE_ERROR": 4,
        "OK": 5,
        "ACCEPTED": 6,
        "WRONG_ANSWER": 7,
        "RUNTIME_ERROR": 8,
        "TIME_LIMIT_EXCEEDED": 9,
        "CANT_BE_JUDGED": 10,
        "REJUDGE_REQUESTED": 11}

class Submission(models.Model):
    submitted = models.DateTimeField(null=True, auto_now_add=True)
    problem = models.ForeignKey(Problem, null=True, db_index=True)
    is_public = models.BooleanField(default=False)
    author = models.ForeignKey(User, null=True, db_index=True)
    language = models.CharField(max_length=64, default="")
    state = models.IntegerField(default=SUBMISSION_STATES["RECEIVED"],
            choices=SUBMISSION_STATES.iteritems())
    length = models.IntegerField(default=0)
    source = models.TextField(default="")
    message = models.TextField(null=True)
    time = models.IntegerField(null=True)
    memory = models.IntegerField(null=True)

