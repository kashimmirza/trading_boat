from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
# from celery.schedulers import crontab
os.environ.setdefault('DJANGO_SETTING_MODULE', 'tradingapplication.settings')
app = Celery('tradingapplication')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Dhaka')
app.config_from_object(settings, namespace='CELERY')
app.conf.beat_schedule = {
    'every-10-seconds': {
        'task': 'trade1.tasks.update_stock',
        'schedule': 10,
        'args': (['RELIANCE.NS', 'BAJAJFINSV.NS'],)
    },

}
app.autodiscover_tasks()


@app.task(blind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')