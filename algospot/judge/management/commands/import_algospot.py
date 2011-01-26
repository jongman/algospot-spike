#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from algospot.judge.models import *

class Command(BaseCommand):
    args = '<JSON file path>'
    help = 'Import all data from a JSON file from mysqldumper.'

    def import_problems(self, all):
        Problem.objects.all().delete()
        for problem in all["GDN_Problem"]:
            del problem["no"] # for now
            del problem["author"] # for now
            p = Problem(**problem)
            p.save()
            print "Imported %s." % problem["name"]
        print "Imported %d problems." % len(all["GDN_Problem"])

    def handle(self, *args, **kwargs):
        if len(args) != 1:
            raise CommandError("Specify a single JSON file path.")
        import myjson
        all = myjson.loads(open(args[0]).read())

        self.import_problems(all)
