
from flask_rq2 import RQ

'redis://127.0.0.1:6379/0'
rq = RQ()


# Creates a worker that handle jobs in ``default`` queue.
default_worker = rq.get_worker()
default_worker.work(burst=True)

# Creates a worker that handle jobs in both ``simple`` and ``low`` queues.
low_n_simple_worker = rq.get_worker('low', 'simple')
low_n_simple_worker.work(burst=True)
