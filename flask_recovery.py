import qrcode
import serial
import adafruit_thermal_printer
import subprocess
import time
from PIL import Image, ImageDraw
from bitlyshortener import Shortener
import re
from github import Github
import github
import sqlite3
from flask import Flask
from flask import Flask, flash , redirect , render_template , request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    if str(request.form['pi'])=='pi':
         repository = request.form['repo']
         number_issue=str(request.form['number_issue'])
         time.sleep(2)
         url_recovery='https://github.com/'+os.environ['NAME_ORGANIZZATION']+'/'+repository+'/issues/'+number_issue
         f= open("url.txt","w+")
         f.write(url_recovery)
         f.close()
         from recovery_issue import  select_url
         select_url()
         return render_template('index.html')
    else:
         return render_template('index1.html')
    
    

