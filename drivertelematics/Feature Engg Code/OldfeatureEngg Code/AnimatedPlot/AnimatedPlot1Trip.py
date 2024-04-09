


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pylab import *
import scipy.optimize as optimization



#Animation Plot One Driver One Trip 

def AnimatedPlot1Trip(data):
              
            
    
            #Local Turn Radius
            def turnradiuslocal(xdata,ydata,vdata,adata,tdata):
                        #Fitting Function
                        def func(x, a, b, c):
                                    return a + b*x + c*x*x 
            
            
            
                        
            # Fuction to calculate the radius of curvature
                        def curvatureradius(x,c,a,b):
                                    dy = 2*c*x + b
                                    d2y = 2*c
                                    R = ((1+(dy)**2)**(1.5)) / (abs(d2y))
                                    return R 
                        
                        
                        
                        
                        x0 = np.array([0.0, 0.0, 0.0])
                        para , optimize = optimization.curve_fit(func, xdata, ydata, x0)
                        a = para[0]
                        b = para[1]
                        c = para[2]
                        R=[]
                        for i, xin in enumerate(xdata): 
                                    R.append(curvatureradius(xin,c,a,b))
                        yest=[]
                        for i, xin in enumerate(xdata):
                                    yest.append(a + b*xin + c*xin*xin)
                        slope=[]
                        for i, xin in enumerate(xdata):
                                    slope.append(2*c*xin + b)    
                        return R,xdata,yest,slope,vdata,adata,tdata    
                 
            
            
            x,y,t,trip,driver,v,a = zip(*data)
            xdata= np.array(x)
            ydata= np.array(y)
            tdata = np.array(t)
            vdata = np.array(v)
            adata = np.array(a)
            
            
            #initialize plots
            fig = plt.figure()
            ax = fig.add_subplot(311)
            plt.scatter(xdata,ydata, s=10, color = 'blue')
            line, = plt.plot(xdata[0:11],ydata[0:11], "x", color="red")
            line2, = plt.plot([],[], "o", color="green")
            line3, = plt.plot([],[], "-", color="black")
            tantext = ax.text(0,0,"asda")
            ax2 = fig.add_subplot(312)
            plt.plot(tdata,vdata, "k", color = 'blue' )
            plt.ylabel('Velocity')
            line4, = plt.plot([],[], "o", color="red")
            ax3 = fig.add_subplot(313)
            plt.plot(tdata,adata, "k", color = 'blue' )
            plt.ylabel('Accelaration')
            plt.xlabel('Time')
            line5, = plt.plot([],[], "o", color="red")
            ax3.set_ylim(-5,10)            
    
    
            def update():
                        for i in range(len(xdata)-11):
                                    R = turnradiuslocal(xdata[0+i:11+i],ydata[0+i:11+i],vdata[0+i:11+i],adata[0+i:11+i],tdata[0+i:11+i])
                                    y1 = R[2][5] 
                                    x1 = R[1][5]
                                    x2 = R[1][5] + 10
                                    v = R[4][5]
                                    a = R[5][5]
                                    t = R[6][5]
                                    m  = R[3][5]
                                    m = -1 / m
                                    x=arange((x1-50),(x1+50),.1)
                                    y = y1 + (m * (x - x1) )
                                    y2 = y1 + (m * (x2 - x1) )        
                                    yield R,x,y,x2,y2,v,a,t
    
            def draw(data):
                        R = data[0]
                        x= data[1]
                        y = data[2]
                        x2 = data[3]
                        y2 = data[4]
                        v=data[5]
                        a = data[6]
                        t= data[7]
                        line.set_xdata(R[1])
                        line.set_ydata(R[2])
                        line2.set_xdata(R[1][5])
                        line2.set_ydata(R[2][5])
                        line3.set_xdata(x)
                        line3.set_ydata(y)
                        line4.set_xdata(t)
                        line4.set_ydata(v)
                        line5.set_xdata(t)
                        line5.set_ydata(a)                        
                        tantext.set_position([x2+60,y2+60])
                        textatpoint = 'Driving Down a Straight'
                        ax.set_xlim( ( min(R[1]) - math.copysign(500, min(R[1]) ) ),( max(R[1]) + math.copysign(500, max(R[1]) ) ))
                        ax.set_ylim( ( min(R[2]) - math.copysign(500, min(R[2]) ) ),( max(R[2]) + math.copysign(500, max(R[2]) ) ))
                        if(abs(R[0][5]) < 500):
                                    textatpoint = 'Driving Down a Turn'
                        tantext.set_text(textatpoint)
                        return line,line2,line3
    
            ani = animation.FuncAnimation(fig, draw, update, interval=.001, blit=False)
            
            fig.show()    
    
