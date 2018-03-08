from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world_view():
    return 'Hello World!'


@app.route('/request')
def request_view():
    return f'request method: {request.method} \n url {request.url} \n headersL {request.headers}'


if __name__ == '__main__':
    app.run(debug=True)
