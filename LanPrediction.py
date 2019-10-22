# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:36:01 2019

@author: Banish_Bansal
"""

#IrisClassifier.py
from sklearn.externals import joblib

class LanPrediction(object):
    def __init__(self):
        self.model = joblib.load('lan_prediction.sav')
    # feature_names aren't needed 
    def predict(self,X,features_names):
        return self.model.predict(X)