# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:23:04 2016

@author: dheepan.ramanan
"""


from sklearn import svm
from sklearn.feature_selection import SelectKBest
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import f_regression
from themes_df import oscar_features, labels
from sklearn.cross_validation import cross_val_score

X = oscar_features
y = labels 
anova_filter = SelectKBest(f_regression, k=7)
clf = svm.SVC(kernel='linear')
anova_svm = Pipeline([('anova', anova_filter), ('svc', clf)])
anova_svm.set_params(anova__k=10, svc__C=1).fit(X, y)

prediction = anova_svm.predict(X)
anova_svm.score(X, y)

scores = cross_val_score(clf, X, y, cv=5)    