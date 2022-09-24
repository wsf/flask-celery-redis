from celery import Celery
endpoint = Celery('endpoint',
                  broker="redis://localhost:6379",
                  include=['task'])
