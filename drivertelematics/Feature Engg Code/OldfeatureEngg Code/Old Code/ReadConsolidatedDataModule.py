import csv
import numpy as np
import os
from os import path
import math as math


def ReadConsolidatedData(start_path):
              global start_path
              
              def OneDriverData(dirverdirectory):
              
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
                                                        row.append(driverdirectory)
                                                        data.append(row)
                                          return data
           
              
                            files = os.listdir(dirverdirectory)
                            data = []         
                            for file in files:
                                          filename , ext = file.split('.',2)
                                          filename = int(filename)
                                          file_path = os.path.join(dirverdirectory,file)
                                          data.append(readCsvRows(file_path,filename)) 
                       
          
                            for trip in data:
                                          trip[0].append(0)
                                          for i in list(range(1,len(trip),1)):
                                                        trip[i].append(math.sqrt(math.pow((trip[i][0]-trip[i-1][0]),2) + math.pow((trip[i][1]-trip[i-1][1]),2)))
    
                            for trip in data:
                                          trip[0].append(0)
                                          for i in list(range(1,len(trip),1)):
                                                        trip[i].append(trip[i][4]-trip[i-1][4])
                            return data
    
              dirverdirectories = os.listdir(start_path)
              data = []
              for dirverdirectory in dirverdirectories:
                            Data.append(OneDriverData(dirverdirectory))
                            print dirverdirectory
              return data              




  