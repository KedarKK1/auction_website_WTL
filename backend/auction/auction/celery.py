import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auction.settings')

# app = Celery('auction') # * this worked great
# app = Celery('auction', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0') # ! not working
app = Celery('auction', broker='redis://localhost:6379/0')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Configure Celery
app.conf.task_default_queue = 'auction_queue'
app.conf.task_default_exchange = 'auction_exchange'
app.conf.task_default_routing_key = 'auction_routing_key'



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

from .tasks import check_auction_start

def add_auction_to_queue(auction_id, start_date): # add_auction_to_queue is a function that adds an auction to the queue with a specific start date
    check_auction_start.apply_async(args=[auction_id], eta=start_date) # eta parameter of apply_async is used to specify the execution time of the task.
