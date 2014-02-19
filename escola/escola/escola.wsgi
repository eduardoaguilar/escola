import os, sys
sys.path.append('/var/www/html/escola')
sys.path.append('/var/www/html/escola/escola')
os.environ['DJANGO_SETTINGS_MODULE'] = 'escola.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()