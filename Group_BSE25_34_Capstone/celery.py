import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Group_BSE25_34_Capstone.settings')

app = Celery('Group_BSE25_34_Capstone')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()