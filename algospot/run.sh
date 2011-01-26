#!/bin/bash
echo yes | ./manage.py build_static
./manage.py runserver
