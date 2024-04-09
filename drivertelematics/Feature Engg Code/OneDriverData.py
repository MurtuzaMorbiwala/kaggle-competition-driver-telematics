import csv
import numpy as np
import os
from os import path
import math as math
import FeatureVector_all_data_veri as fv
from numpy import genfromtxt


def OneDriverData(dirverdirectory,driverdirectorypath):

              def readCsvRows(file_path,filename,dirverdirectory):
                            
                            trip = fv.FeatureVector(dirverdirectory,filename,file_path)
                                                                                                        
                            return trip


              files = os.listdir(driverdirectorypath)
              data = []         
              for file in files:
                            filename , ext = file.split('.',2)
                            filename = int(filename)
                            file_path = os.path.join(driverdirectorypath,file)
                            data.extend(readCsvRows(file_path,filename,dirverdirectory)) 
         

              return data

              



  