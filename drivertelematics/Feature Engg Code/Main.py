# Main Module

import numpy as np
import OneDriverData as odd
import warnings
import os
from os import path
import random

warnings.filterwarnings('ignore')


start_path = 'C:\\Users\\murtuzam\\Desktop\\drivertelematics\\inputdata\\drivers'
drivers = os.listdir(start_path)
print drivers
#featuredata = []


#drivers = drivers[0:2]




#for driver in drivers:
    #print driver
    #dirverdirectoy = os.path.join(start_path,driver)
    #data = odd.OneDriverData(driver,dirverdirectoy)
    #featuredata.extend(data)
    
    

#outpath =  'C:\\Users\\murtuzam\\Desktop\\drivertelematics\\outputdata\\features_final.csv'

#print featuredata

#import csv

#with open(outpath, "wb") as f:
    #writer = csv.writer(f)
    #writer.writerows(featuredata)   
    
    
    #i = drivers.index('1')
    #driver = drivers[i]
    #other_drivers = drivers
    #other_drivers.pop(i)
    
    
    #random_drivers = random.sample(other_drivers, 5)
    
    #random_drivers.append(driver)
    
    #print random_drivers    