import TripTurnRadius as ttr 
import numpy 
import numpy as np 
 




 
def FeatureVector(driver,triplabel,path): 
     
    def movingaverage(values,window): 
        weights=np.repeat(1.0,window)/window 
        smas = np.convolve(values,weights,'valid') 
        return smas 
 
 
 
    tripfeature = [] 
    trip = numpy.loadtxt(path, delimiter=',',skiprows = 1 ) 
    trip = numpy.transpose(trip) 
    x = trip[0] 
    y = trip[1] 
    
    x1 = numpy.delete(x, -1) 
    x1 = numpy.insert(x1,0,0) 
    y1 = numpy.delete(y, -1) 
    y1 = numpy.insert(y1,0,0) 
    v = ((x-x1)**2 + (y-y1)**2)**(.5)  
    r = ttr.TripTurnRadius(x,y) 
    r = movingaverage(r,3)  
    v = movingaverage(v,3) 
    vr = v[r<1000]/r[r<1000] 
    v1 = numpy.delete(v, -1) 
    v1 = numpy.insert(v1,0,0) 
    a = v-v1       
    av = v*a 
    a = movingaverage(a,3)   
    a1 = numpy.delete(a, -1) 
    a1 = numpy.insert(a1,0,0) 
    j = a-a1 
    j = movingaverage(j,3)    
    av = movingaverage(a,3)   
    a = numpy.delete(a,[0,1,2])
    av = numpy.delete(av,[0,1,2]) 
    j = numpy.delete(j,[0,1,2])
    
    
 
    
     
    if len(vr) == 0 : 
        vr = numpy.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) 
 
     
     
    vr[numpy.isnan(vr)] = 0 
     
    
    total_time  =  len(x) 
    total_distance = sum(v)       
     
    mean_v = numpy.mean(v) 
    mean_a = numpy.mean(a) 
    mean_vr = numpy.mean(vr)           
    mean_j = numpy.mean(j)
    vel_q = numpy.percentile(v, range(0,105,5) )   
    acc_q = numpy.percentile(a, range(0,105,5) ) 
    av_q = numpy.percentile(av, range(0,105,5) ) 
    vr_q  = numpy.percentile(vr, range(0,105,5))        
    j_q  = numpy.percentile(j,range(0,105,5))
    vel_bin = numpy.histogram(v,range(0,60,10)) 
    vel_bin = vel_bin[0]       
    tripfeature = [driver,triplabel,total_time,total_distance,mean_v,mean_a,mean_vr,mean_j] 
    tripfeature.extend(vel_q) 
    tripfeature.extend(acc_q) 
    tripfeature.extend(vr_q) 
    tripfeature.extend(vel_bin) 
    tripfeature.extend(av_q) 
    tripfeature.extend(j_q)
    return tripfeature



driver = 1
triplabel = '1'
path = 'C:/Users/murtuzam/Desktop/drivertelematics/inputdata/drivers/1/1.csv'

fv = FeatureVector(driver,triplabel,path)
print fv