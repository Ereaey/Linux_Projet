import serial
import os
import time
import sys
sys.path.append("/home/debian/logiciel_beaglebone/common_dbus")
from protocole import *

from bottle import Bottle, run, view, request, static_file
 
app = Bottle()
p = Protocole()

@app.route('/')
@view('/home/debian/logiciel_beaglebone/site_dbus/index.tpl')
def hello():
    e = []
    a = {'id':0, 'name':'square'}
    e.append(a)
    a = {'id':1, 'name':'circle'}
    e.append(a)
    a = {'id':2, 'name':'spiral'}
    e.append(a)
    a = {'id':3, 'name':'triangle'}
    e.append(a)
    return {"title":"Domotique","menu": e, "equipments" : ""}

@app.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='.')
    
@app.route('/draw/:shape')
def draw(shape):
    p.drawShape(shape)
    return shape


run(app, host='', port=8080)