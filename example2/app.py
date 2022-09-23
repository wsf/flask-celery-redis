from flask import Flask
from flask_rq2 import RQ
import time

app = Flask(__name__)
app.config['RQ_REDIS_URL'] = 'redis://127.0.0.1:6379/0'

rq = RQ(app)

f = open("result.log",'w')

@rq.job
def foo(a,b):
    print(a+b)
    f.write(str(a+b))
    f.close()
    time.sleep(a)
    return a + b;


@app.route('/')
def index():
    job = foo.queue(5,9)
    job2 = foo.queue(5, 9)
    job3 = foo.queue(1, 9)
    job4 = foo.queue(2, 9)
    job5 = foo.queue(3, 9)

    print(foo.queue(8,8))



    return 'Job queued!'



if __name__ == "__main__":
    app.run(port=5000, debug=True)
