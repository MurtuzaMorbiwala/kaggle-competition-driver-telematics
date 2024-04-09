import csv
import numpy as np
import os
from os import path
import math as math


def ReadData(start_path):             
              
              def OneDriverData(dirverdirectory,driverdirectorypath):
              
                            def readCsvRows(file_path,filename,dirverdirectory):
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
                                                                      row.append(int(dirverdirectory))
                                                                      data.append(row)
                                          return data
           
              
                            files = os.listdir(driverdirectorypath)
                            data = []         
                            for file in files:
                                          filename , ext = file.split('.',2)
                                          filename = int(filename)
                                          file_path = os.path.join(driverdirectorypath,file)
                                          data.append(readCsvRows(file_path,filename,dirverdirectory)) 
                       
          
                            return data
    
              dirverdirectories = os.listdir(start_path)
              data = []
              for dirverdirectory in dirverdirectories:
                            driverdirectorypath =  os.path.join(start_path,dirverdirectory)
                            data.append(OneDriverData(dirverdirectory,driverdirectorypath))
                            
              return data              




  