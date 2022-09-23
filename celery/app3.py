from flask import Flask, jsonify
from celery import Celery


app = Flask(__name__)
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379"

celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)


@celery.task()
def add(x, y):
    f = open('eject.log', 'a')
    f.write(str(x))
    f.close()


@app.route('/')
def add_task():
    for i in range(10):
        add.delay(i, i)

    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(port=5000, debug=True)