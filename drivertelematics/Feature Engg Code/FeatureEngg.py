
import math
import TripTurnRadius as ttr
import numpy
import bisect

def FeatureEngg(trip):
        
                
        driver  = max(driverdata)
        trip = max(tripdata)
        total_time  =  max(tdata)
        total_distance = sum(vdata)      
        mean_v = numpy.mean(vdata)
        mean_a = numpy.mean(adata)
        mean_vr = numpy.mean(vrdata)          
        vel_q = numpy.percentile(vdata, range(0,105,5) )  
        acc_q = numpy.percentile(adata, range(0,105,5) )
        vr_q  = numpy.percentile(vrdata, range(0,105,5))       
                
        tripfeature = [driver,trip,total_time,total_distance,mean_v,mean_vr,mean_a]
        tripfeature.extend(vel_q)
        tripfeature.extend(acc_q)
        tripfeature.extend(vr_q)
                
        features.append(tripfeature)
        
        
            
        return features
