#!/usr/bin/env python
'''
 adt7310_test.py 
 Rekha Seethamraju

 An example to demonstrate the use of the ADT7310 library
 for PyBBIO.

 This example program is in the public domain.
'''
from bbio import *
from ADT7310 import *

adt = ADT7310(0,0)
pin = GPIO1_28  
pinc = GPIO0_4

def alarm():
  '''executed when temp crosses threshold temperatures - high and low '''
  print("Too Hot or Cold!")

def criticalalarm():
 '''executed when temp crossed critical temperature '''
  print("Over Critical Temperature")

def setup():
  #sets low temperature threshold
  adt.setLowTemp(5)
  #sets high temperature threshold
  adt.setHighTemp(50)
  #sets high temperature threshold
  adt.setCriticalTemp(60)
  #sets the function to call when interrupt pin in active.
  adt.setAlarm(pin,alarm)
  #sets the function to call when interrupt pin in active.
  adt.setCriticalAlarm(pin,criticalalarm)
    
def loop():
  temp = adt.getTemp() 
  print "temperature : "+str(temp)
  delay(500)  
  
run(setup,loop)