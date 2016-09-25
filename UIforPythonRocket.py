import Tkinter
from tkinter import *
import math
import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy as np
from numpy import arange, sin, pi
from scipy import interpolate
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

def main():
    root = makeInterface()
    #print root.winfo_children()[5].text()
    #e2.grid(row=1, column=1)
    root.mainloop()

def getInputs(exhaustVel, payload, fuelLoad, burnRate):
    return exhaustVel.get(), payload.get(), fuelLoad.get(), burnRate.get()
    root.mainloop()

def isClicked(root):
    haveLabel = len(root.winfo_children())
    if haveLabel == 11:
        undrawLabels(root.winfo_children()[10])
    ve = root.winfo_children()[6]
    payload = root.winfo_children()[7]
    fuelLoad = root.winfo_children()[8]
    burnRate = root.winfo_children()[9]
    vez, payloadz, fuelLoadz, burnRatez =getInputs(ve, payload, fuelLoad, burnRate)
    graph, maxHeight, time = heightVtime(float(vez), float(payloadz), float(fuelLoadz), float(burnRatez))
    label,a = makeLabels(root, maxHeight, time)
    drawLabels(root, label, a, graph)

def makeInterface():
    root = Tkinter.Tk()
    root.geometry("900x600+300+300")
    Calculate = Tkinter.Button(text ="Calculate", width=10 ,command= lambda: isClicked(root) )
    Calculate.place(relx=.1, rely=.4, anchor="c")
    Quit = Tkinter.Button(text ="Quit", width=10 ,command = lambda : root.destroy())
    Quit.place(relx=.1, rely=.47, anchor="c")
    label1 = Label(  text="Exhaust Velocity")
    label1.place(relx=0, rely=.1)
    label2 = Label(  text="Payload")
    label2.place(relx=0, rely=.17)
    label3 = Label(  text="Fuel Load")
    label3.place(relx=0, rely=.24)
    label4 = Label(  text="Fuel Burn Rate")
    label4.place(relx=0, rely=.31)
    e1 = Entry(root,width =7)
    e2 = Entry(root,width =7)
    e3 = Entry(root,width =7)
    e4 = Entry(root,width =7)
    e1.place(relx=.11, rely=.1)
    e2.place(relx=.11, rely=.17)
    e3.place(relx=.11, rely=.24)
    e4.place(relx=.11, rely=.31)
    return root

def heightVtime(ev,p,f,b):
    m=p+f
    x=[0]
    y=[0]
    t= f/b
    m=p+f
    count = 0.1
    v=0
    g=9.8
    hprev = 0
    h=0
    vmax  = 0
    while count <t :
        v = ev*math.log(m - b*count) - g*count
        if v > vmax:
            vmax = v
        x.append(count);
        h = hprev + v*(0.1)
        y.append(h)
        hprev = h
        count=count+0.1
    maxHeight = h
    while h > 0 :
        z= vmax - 0.1
        h = hprev - z * 0.1
        x.append(count)
        if  h < 0:
            y.append(0)
        else :
            y.append(h)
        count = count + 0.1
        hprev = h
    graph = []
    graph.append(x)
    graph.append(y)
    return graph, maxHeight, count

def makeLabels(root, t, hmx):
    label = Figure(figsize=(7,5.6), dpi=100)
    a = label.add_subplot(111)
    return label,a;

def drawLabels(root, label, a, graph):
    a.plot(graph[0],graph[1])
    dataPlot = FigureCanvasTkAgg(label, master=root)
    dataPlot.get_tk_widget().place(relx = 0.2 ,rely = 0.03)

def undrawLabels(label):
    label.destroy()



main()
