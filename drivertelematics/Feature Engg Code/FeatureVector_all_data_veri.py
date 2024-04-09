import TripTurnRadius as ttr
import numpy
import os


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
    #r = ttr.TripTurnRadius(x,y)
    #vr = v/r
    
    #vr[numpy.isnan(vr)] = 0
    
    
    driver_a = [str(driver) for i in v]
    trip_a = [triplabel for i in v]
    
    
    
    tripfeature = numpy.column_stack((driver_a,trip_a,v,a))
    
    
    
    return tripfeature


      
