"""
WSGI config for FacebookTest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

activate_this = '/home/virtualenvdemo/.virtualenvs/django16/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys

path = '/home/virtualenvdemo/FacebookTest'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'FacebookTest.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()