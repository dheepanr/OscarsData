# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:19:30 2016

@author: dheepan.ramanan
"""


import pickle
import pandas as pd

themes_df = pickle.load(open('/Users/dheepan.ramanan/Documents/OscarsData/DataFilespickle4.p','rb'))

def rerrange(themes_df):
	newdict={}
	for key, theme in themes_df.items():
		newindex = key[0]
		themeName = key[1]
		if newindex not in newdict:
			newdict[newindex] = {}
		else:
			for datapoint, data in theme.items():
				uniqueDataPoint = str(themeName)+'_'+str(datapoint)
				newdict[newindex][uniqueDataPoint] = data
	return newdict

new_df = pd.DataFrame.from_dict(rerrange(themes_df)).T

def binary(status):
	if status == 'winner':
		status= 1
	else:
		status = 0
		
	return status

data = pd.read_excel('/Users/dheepan.ramanan/Documents/OscarsData/dropboxoscars.xlsx')
data['boxoffice'].astype(int)
data['status'] = data.winner.apply(lambda x : binary(x))			
data['status'].astype(int)
movies_agg = data.groupby('movietitle').mean()
complete_oscar = movies_agg.join(new_df)
complete_oscar = complete_oscar.fillna(0)

oscar_features = complete_oscar.drop('status',1)
labels = complete_oscar.status