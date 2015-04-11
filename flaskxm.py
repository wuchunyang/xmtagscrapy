#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from flask import Flask
from flask import request
import json
import xiamiscrapy

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

@app.route('/searchtags/')
def hello_world():

    if request.method == 'GET':
        return json.dumps(xiamiscrapy.search(request.args.get('song',''), request.args.get('singer','')))

    return 'oops,something was wrong!'

@app.route('/user/<username>')
def user(username):
    return 'hello %s' % username

@app.route('/id/<int:num>/')
def hid(num):
    return 'num %d' % num

if __name__ == '__main__':
//    app.debug = True
    app.run()
