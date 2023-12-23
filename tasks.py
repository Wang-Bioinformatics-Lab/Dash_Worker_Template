from celery import Celery
import glob
import sys

celery_instance = Celery('tasks', backend='redis://template-dash-redis', broker='pyamqp://guest@template-dash-rabbitmq//', )

@celery_instance.task(time_limit=60)
def task_computeheartbeat():
    print("UP", file=sys.stderr, flush=True)
    return "Up"

celery_instance.conf.task_routes = {
    'tasks.task_computeheartbeat': {'queue': 'worker'},
}