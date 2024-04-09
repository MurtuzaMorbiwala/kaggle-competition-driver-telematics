import numpy as np
import scipy.optimize as optimization

import warnings
warnings.filterwarnings('ignore')




def TripTurnRadius(xdata,ydata):        
            #Local Turn Radius
            def turnradiuslocal(xdata,ydata):
                        #Fitting Function
                        def func(x, a, b, c):
                                    return a + b*x + c*x*x 
            
            
            
                        
            # Fuction to calculate the radius of curvature
                        def curvatureradius(x,c,a,b):
                                    dy = 2*c*x + b
                                    d2y = 2*c
                                    try:
                                                R = ((1+(dy)**2)**(1.5)) / (abs(d2y))
                                    except ZeroDivisionError:
                                                R = 0 
                                    return R 
                        
                        
                        
                        
                        x0 = np.array([0.0, 0.0, 0.0])
                        try:
                                    para , optimize = optimization.curve_fit(func, xdata, ydata, x0)   
                                    a = para[0]
                                    b = para[1]
                                    c = para[2]
                        except RuntimeError:
                                    a=0
                                    b=0
                                    c=0
                                    
                        
                        R=[]
                        for i, xin in enumerate(xdata): 
                                    R.append(curvatureradius(xin,c,a,b))
                        return R
            
            
                        
            
            R = xdata 
            R = [0 for rin in R]
            
            
            for i in range(5,len(xdata)-5):
                        LR = turnradiuslocal(xdata[i-5:i+6],ydata[i-5:i+6]) 
                        R[i]=float(LR[5])
                        
            #Handling Exceptions
            
            LR = turnradiuslocal(xdata[0:11],ydata[0:11])
            R[0:5] = LR[0:5]
                 
            LR = turnradiuslocal(xdata[len(xdata)-11:len(xdata)],ydata[len(xdata)-11:len(xdata)])
            R[len(xdata)-5:len(xdata)] = LR[6:11]
            
                               
                        
                             
            
            R = np.array(R)
            
            R[R>1000] = 1000
            R[R<1] = 1
            
            R[np.isnan(R)] = 0
            R[np.isinf(R)] = 1000             
                     
                       
                       
            return R
           
           
     