import numpy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score
from itertools import groupby
import itertools
from operator import itemgetter
import random

import cPickle as pickle
from sklearn.externals import joblib


start_path = 'C:\Users\murtuzam\Desktop\drivertelematics\outputdata\\InputModel\\features.csv'

trips = np.loadtxt(open(start_path, 'r'), dtype='f8', delimiter=',')

trips_pk1_path =  'C:\Users\murtuzam\Desktop\drivertelematics\outputdata\\InputModel\\features.pk1'

joblib.dump(trips, trips_pk1_path)