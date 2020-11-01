from wsgiref.simple_server import make_server
from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/hello-world-5')
def hello_world():
    return 'Hello World 5'


with make_server('', 5000, app) as server:
    print("Something http://127.0.0.1:5000")

    server.serve_forever()
