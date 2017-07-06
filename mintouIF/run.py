#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing


from flask import Flask, render_template
import os

app = Flask(__name__)
imagepath = os.path.join(os.getcwd(),"static/images")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    os.system("python starttest.py")
    return render_template('index.html')

@app.route('/start', methods=['GET'])
def start():
    return render_template('indexload.html')

@app.route('/report', methods=['GET'])
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(host='172.16.0.8',port=5000,debug=True)