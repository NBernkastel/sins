import os

import serial
import matplotlib.pyplot as plt
from pynput.mouse import Controller, Button
ser = serial.Serial(port='COM5', baudrate=9600, timeout=2)
y = []
x = []
k = 0
mouse = Controller()
sens = 3
while 1:
    i = 0
    data = []
    while i < 6:
        try:
            data.append(int(ser.readline().decode('windows-1251'))/16000)
        except ValueError:
            continue
        i+=1
    # if data[4] > 1:
    #    mouse.press(Button.left)
    #    mouse.release(Button.left)
    if data[1] > 0 and data[1] > 0.05:
        mouse.move(0,data[1]*sens)
    if data[1] < 0 and data[1] < -0.05:
        mouse.move(0,data[1]*sens)
    if data[0] > 0 and data[0] > 0.05:
        mouse.move(data[0]*sens,0)
    if data[0] < 0 and data[0] < -0.05:
        mouse.move(data[0]*sens,0)
    #print(data[1]*50)
 #    y.append(data[0])
 #    x.append(k)
 #    if len(x) > 100:
 #        x.pop(0)
 #        y.pop(0)
 #   # if data >= 0.5:
 #   #     mouse.scroll(dx=0,dy=1)
 #   #  if data < 1:
 #     #   firs = 0
 # #   if data <= -0.5:
 # #       mouse.scroll(dx=0, dy=-1)
 #    #print(format(data,'.2f'))
 #    plt.plot(x,y)
 #    plt.ylim(-1.1,1.1)
 #    k += 1
 #    plt.draw()
 #    plt.pause(0.001)
 #    plt.clf()



