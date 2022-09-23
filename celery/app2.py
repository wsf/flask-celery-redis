from celery import Celery
from flask import Flask

app = Flask(__name__)

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/do")
def do():
    global task
    task = divide.delay(1, 2)


    return (str(task.result) +   " " + str(task.state))

@app.route("/do_result")
def do_result():
    f = open('./eject.log', 'a')
    f.write('vv')
    f.close()


    global task
    return (str(task.result) +   "--------- " + str(task.state))

@celery.task
def divide(x, y):

    f = open('./eject.log','a')
    f.write(str(x))

    import time
    time.sleep(1)
    f.write(str(y))


    f.close()
    return x / y

if __name__ == "__main__":
    app.run(port=5000, debug=True)