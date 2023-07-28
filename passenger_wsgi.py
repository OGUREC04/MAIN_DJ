# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/n/nicharnj/nicharnj.beget.tech/MAIN_DJ')
sys.path.insert(1, '/home/n/nicharnj/nicharnj.beget.tech/venv_django/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'MAIN_DJ.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()