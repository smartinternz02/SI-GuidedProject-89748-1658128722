#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 18:45:49 2022

@author: suryadevaramukesh
"""

from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('chatbot.html')

if __name__=='__main__':
    app.run(debug=False,host='8000')
    
    