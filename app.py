from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/hello-world-<var>')
def hello_world(var):
    return 'Hello World' + str(var)


if __name__ == '__main__':
    app.run()
