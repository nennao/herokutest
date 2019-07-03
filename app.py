from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def route_test():
    return 'Testing testing 123...'


if __name__ == '__main__':
    app.run()
