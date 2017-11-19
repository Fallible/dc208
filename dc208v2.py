import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')
#def hello_world():
#    return 'Hello World!'

@app.route('/Calendar')
def calendar():
    return render_template('/Calendar.html')

@app.route('/Comms')
def comms():
    return render_template('/Comms.html')


if __name__ == '__main__':
    app.run()
