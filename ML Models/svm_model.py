# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:23:04 2016

@author: dheepan.ramanan
"""


from sklearn import svm
from sklearn.feature_selection import SelectPercentile
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import f_classif
from themes_df import oscar_features, labels
from sklearn.cross_validation import cross_val_score
from sklearn import metrics


X = oscar_features.drop(["index","year"],1)
feature_names = X.columns.values
y = labels 

anova_filter = SelectPercentile(f_classif)
clf = svm.SVC(probability=True)
accuracy=[]
percentile_range = range(1,100,2)

for p in percentile_range:
	
	anova_filter = SelectPercentile(f_classif, percentile=p)
	anova_svm = Pipeline([('anova', anova_filter), ('svc', clf)])
	anova_svm.set_params(anova__p=p, svc__C=1).fit(X, y)
	prediction = anova_svm.predict(X)
	score = anova_svm.score(X, y)
	cv = cross_val_score(clf, X, y, scoring ="accuracy",cv=5)
	

	accuracy.append(cv)

p_values = anova_filter
feature_importance = zip(feature_names,p_values)

probabilities = zip(X.index.tolist(),anova_svm.predict_proba(X))
