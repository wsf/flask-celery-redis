from flask import Flask, jsonify
from celery import Celery
from task import add

app = Flask(__name__)

@app.route('/')
def add_task():
    for i in range(10):
        task = add.delay(i, i)
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(port=5000, debug=True)