
import math
import TripTurnRadius as ttr
import numpy
import bisect

def FeatureEngg(driver):
        
        features = []
        
        

        for trip in driver:
                trip[0].append(0)
                for i in list(range(1,len(trip),1)):
                        trip[i].append(math.sqrt(math.pow((trip[i][0]-trip[i-1][0]),2) + math.pow((trip[i][1]-trip[i-1][1]),2)))
    
        for trip in driver:
                trip[0].append(0)
                for i in list(range(1,len(trip),1)):
                        trip[i].append(trip[i][5]-trip[i-1][5])
        
      
        
           
        for i,trip in enumerate(driver):
                tripfeature = []
                
                xdata,ydata,tdata,tripdata,driverdata,vdata,adata = zip(*trip)        
                adata = numpy.array(adata)
                vdata = numpy.array(vdata)
                driver  = max(driverdata)
                trip = max(tripdata)
                total_time  =  max(tdata)
                total_distance = sum(vdata)      
                mean_v = numpy.mean(vdata)
                mean_a = numpy.mean(adata)          
                vel_q = numpy.percentile(vdata, range(0,105,5))  
                acc_q = numpy.percentile(adata, range(0,105,5)) 
                
                tripfeature = [driver,trip,total_time,total_distance,mean_v,mean_a]
                tripfeature.extend(vel_q)
                tripfeature.extend(acc_q)
                
                features.append(tripfeature)
        
        
            
        return features
