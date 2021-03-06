"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
