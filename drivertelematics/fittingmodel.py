import numpy
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score


def fittingmodel(driver , random_drivers):
    X_driver_label =  driver[:,0:2]
    X_driver = driver[:,2:48]
    X_random_drivers = random_drivers[:,2:48]
    Y_driver = [1 for i in driver[:,0]]
    Y_random_drivers = [-1 for i in random_drivers[:,0]]
    X = numpy.concatenate((X_driver,X_random_drivers))
    y = numpy.concatenate((Y_driver,Y_random_drivers))
    clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=10),algorithm="SAMME",n_estimators=100).fit(X,y)
    pred_proba = clf.predict_proba(X_driver)[:,1]
    return  numpy.column_stack((X_driver_label,pred_proba)) 