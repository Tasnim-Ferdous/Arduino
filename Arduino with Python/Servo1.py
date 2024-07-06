import serial
from vpython import *
import numpy as np

arduinoData = serial.Serial("com3", 115200)

scene.width = 1000
scene.height = 600

boxx = 4
boxy = boxx/2
boxz = 0.1

backgroundBox = box(size=vector(boxx, boxy, boxz), pos= vector(0,0,-0.1))

yfactor = -(boxy/2.25)
arrowlength = boxx/2.8
arrowwidth = arrowlength/60

arr = arrow(length=arrowlength, shaftwidth=arrowwidth, color=color.red, axis=vector(1,0,0), pos=vector(0,yfactor,0))

ticksizex = boxx/45
ticksizey = ticksizex/6
ticksizez = 0.01

for angle in np.linspace (0, np.pi, 37):
    tick = box(size=vector(ticksizex,ticksizey,ticksizez), color=color.black, axis=vector(arrowlength*np.cos(angle), arrowlength*np.sin(angle), 0), pos=vector(arrowlength*np.cos(angle), arrowlength*np.sin(angle)+yfactor, 0))

smallticksizex = ticksizex/1.5
smallticksizey = smallticksizex/5.5
smallticksizez = 0.01

for angle in np.linspace (0, np.pi, 181):
    smalltick = box(size=vector(smallticksizex,smallticksizey,smallticksizez), color=color.black, axis=vector(arrowlength*np.cos(angle), arrowlength*np.sin(angle), 0), pos=vector(arrowlength*np.cos(angle), arrowlength*np.sin(angle)+yfactor, 0))

numsize = ticksizex/2
cnt = 0
numf = 1.07

for angle in np.linspace (0, np.pi, 37):
    ticknum = text(align="center", text=str(cnt), height=numsize, color=color.black, axis=vector(arrowlength*np.cos(angle-np.pi/2), arrowlength*np.sin(angle-np.pi/2), 0), pos=vector(numf*arrowlength*np.cos(angle), numf*arrowlength*np.sin(angle)+yfactor, 0))
    cnt += 5

while True:
    cmd = input("Enter your angle: ")
    cmd = cmd + "\r"
    arduinoData.write(cmd.encode())

    deg = int(cmd.strip("\r"))
    if deg > 180:
        deg = 180
    elif deg < 0:
        deg = 0
    theta = np.pi/180*deg
    arr.axis = vector(arrowlength*np.cos(theta), arrowlength*np.sin(theta), 0)

    amount = label(size=vector(numsize*5, numsize*10, 0), color=color.black, text=str(deg))