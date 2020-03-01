# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:43:08 2020

@author: midhun
"""

from sklearn import ensemble
0.75091
MODELS = {
    "randomforest": ensemble.RandomForestClassifier(n_estimators=200, n_jobs=-1, verbose=2),
    "extratrees": ensemble.ExtraTreesClassifier(n_estimators=200, n_jobs=-1, verbose=2),
}