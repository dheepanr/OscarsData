# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:15:02 2016

@author: dheepan.ramanan
"""
from __future__ import division
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from themes_df import oscar_features, labels
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#lets drop some of the confounding rating variables
X = oscar_features.drop(["index","year","releaseyear","totalfloat","reviewagg"],1)
feature_names = X.columns.values
y = labels

scores = [] 
#tree test
percentile = range(5,150,1)
per_oob_error = []
features_scores = {}
#test for feature inclusion
for p in percentile:
	clf = RandomForestClassifier(n_estimators=125, max_features =p/len(X.columns), oob_score= True, n_jobs=-1)
	clf.fit(X,y)
	prediction = clf.predict(X)
	score = clf.score(X,y)
	scores.append(score)
	features = zip(X.columns.values.tolist(), clf.feature_importances_)
	confusion = metrics.confusion_matrix(y, prediction)
	per_oob_error.append(1-clf.oob_score_)
	features_scores[p] = features
#plotting the error rate
sns.set_style("darkgrid")
plt.plot( percentile, per_oob_error)
plt.xlabel("Number of Features")
plt.ylabel("Out of Bag Error Rate %")
plt.show()

#sort by num features v oob
oob = pd.DataFrame(per_oob_error,percentile, columns=["oob"])
#high feature density, lowest oob
oob[oob["oob"] <.05]
#less feaures
oob[(oob["oob"] >.05) & (oob["oob"] <.08)].head(10)
#closer to sqrt
oob[(oob["oob"] < .1)].head(10)

#load in new dataset 
oscars2016 = pd.read_excel('/Users/dheepan.ramanan/Documents/OscarsData/DataGathering/2016movies2.xlsx')
oscars16themes = pd.read_pickle('/Users/dheepan.ramanan/Documents/OscarsData/DataFiles/oscars16.p')
oscars2016grp = oscars2016.groupby("movietitle").mean()

PredictionOscars = oscars2016grp.join(oscars16themes).fillna(0).drop(["year","releaseyear","totalfloat","reviewagg"],1)










