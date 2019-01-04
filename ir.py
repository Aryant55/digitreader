import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time
import math
import functools as f
from collections import Counter

def createexamplefile():
    newfile = open('numar.txt','a')
    number = range(0,10)
    version = range(1,10)
    
    for eachnum in number:
        for eachver in version:
            filepath = 'images/numbers/'+str(eachnum)+'.'+str(eachver)+'.png'
            ei = Image.open(filepath)
            exar = np.array(ei)
            exar1 = str(exar.tolist())
            ltw =  str(eachnum)+'::'+exar1+'\n'
            newfile.write(ltw)
            
createexamplefile()

def threshold(imgarr):
    barr = []
    newar = imgarr
    
    for eachrow in imgarr:
        for eachpix in eachrow:
            avgnum = f.reduce(lambda x,y:x+y,eachpix[:3])/3
            barr.append(avgnum)
    
    balance = f.reduce(lambda x,y:x+y,barr)/len(barr)
    
    for eachrow in newar:
        for eachpix in eachrow:
            
            if f.reduce(lambda x,y:x+y,eachpix[:3])/3>balance:
                eachpix[0] = 255
                eachpix[2] = 255
                eachpix[1] = 255
            else:
                eachpix[0] = 0
                eachpix[1] = 0
                eachpix[2] = 0
            
            eachpix[3] = 255
    
    return newar

def define(filepath):
    matched = []
    loadex = open('numar.txt','r').read()
    loadex = loadex.split('\n')
    i = Image.open(filepath)
    iar = np.array(i)
    iar1 = iar.tolist()
    inquestion = str(iar1)
    for eachex in loadex:
        if(len(eachex)<3):
            break
        splitex = eachex.split('::')
        currentnum = splitex[0]
        currentar = splitex[1]
        print(currentnum)
        eachpix = currentar.split('],')
        eachpixinq = inquestion.split('],')
        x = 0
        while x<len(eachpix):
            if(eachpix[x]==eachpixinq[x]):
                matched.append(currentnum)
            x+=1
    
    x = Counter(matched)
    
    print(x)
    graphX = []
    graphY = []
    
    ylimi = 0
    
    for i in x:
        graphX.append(i)
        graphY.append(x[i])
        ylimi = x[i]
        
    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)
    
    ax1.imshow(iar)
    ax2.bar(graphX,graphY,align = 'center')
    plt.ylim(400)
    
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()
        
define('images/numbers/1.1.png')


'''
i = Image.open('images/numbers/y0.5.png')
iar = np.array(i)
threshold(iar)
print (iar)

plt.imshow(iar)
plt.show()
i = Image.open('images/numbers/y0.5.png')
iar = np.asarray(i)
print (iar)

plt.imshow(iar)
plt.show()'''