import matplotlib.pyplot as plt
import csv
import numpy as np
import os
from os import path
import math as math





def readCsvRows(file_path,filename):
          
          with open(file_path, 'r') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=',')
                    next(spamreader)
                    i = 0 
                    data = [] 
                    for row in spamreader:
                              row = map(float,row)
                              row.append(i)
                              i=i+1
                              row.append(filename)
                              data.append(row)

                    return data
                    
              


           
start_path = 'C:\\1'
 
files = os.listdir(start_path)
data = []         
for file in files:
          filename , ext = file.split('.',2)
          filename = int(filename)
          file_path = os.path.join(start_path,file)
          data.append(readCsvRows(file_path,filename)) 
          
          
          
      
for trip in data:
          trip[0].append(0)
          for i in list(range(1,len(trip),1)):
                    trip[i].append(math.sqrt(math.pow((trip[i][0]-trip[i-1][0]),2) + math.pow((trip[i][1]-trip[i-1][1]),2)))

for trip in data:
          trip[0].append(0)
          for i in list(range(1,len(trip),1)):
                    trip[i].append(trip[i][4]-trip[i-1][4])


counter = 0
for i in range(12,24):
          counter = counter + 1 
          x,y,t,trip,v,a = zip(*data[i])
          v = np.array(v)
          plt.subplot(2,6,counter,title = set(trip))
          plt.hist(v / 0.44704,10)




plt.show()    


  