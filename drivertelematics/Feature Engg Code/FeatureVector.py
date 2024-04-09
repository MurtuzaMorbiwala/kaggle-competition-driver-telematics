import TripTurnRadius as ttr
import numpy


def FeatureVector(driver,triplabel,path):
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
    v1 = numpy.delete(v, -1)
    v1 = numpy.insert(v1,0,0)
    a = v-v1
    r = ttr.TripTurnRadius(x,y)
    vr = v/r
    
    vr[numpy.isnan(vr)] = 0
    
    driverarr = [driver for i in v]
    
     
    tripfeature
    tripfeature.extend(vel_q)
    tripfeature.extend(acc_q)
    tripfeature.extend(vr_q)
    
    return tripfeature
