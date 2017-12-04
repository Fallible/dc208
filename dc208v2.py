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

@app.route('/News')
def news():
    return render_template('/News.html')

@app.route('/Members')
def members():
    return render_template('/Members.html')

@app.route('/Projects')
def projects():
    return render_template('/Projects.html')

@app.route('/Page_Color')
def page_color():
    return render_template('/Page_Color.html')

@app.route('/Spaces')
def spaces():
    return render_template('/Spaces.html')

@app.route('/inComments')
def in_comments():
    return render_template('/inComments.html')


if __name__ == '__main__':
    app.run()
