# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:55:33 2016

@author: dheepan.ramanan
"""

import pandas as pd
import requests as rq
import json

movienames = pd.read_excel('movienames.xlsx')
movienames = movienames[0].tolist()
headers = {'content-type': 'application/json'}
url = 'https://dexter.clarabridge.net/cbrestfulapi/v1/report'
frames= []

def themeApiCalls(url, authDexter, headers,filtername):
	payload = {'additionalFilters': [filtername],
	 'additionalMetrics': [],
	 'attribute': 1,
	 'count': '50',
	 'direction': 'DESC',
	 'filters': [],
	 'modelId': 78813,
	 'nodeName': 'Movie Model',
	 'page': {'lookAheadLimit': 50},
	 'project': 78514,
	 'projectName': 'Movie Reviews',
	 'reportType': 'TOPICLEAF',
	 'sample': 'full',
	 'selectedNodes': {},
	 'sort': 'volume',
	 'topBottom': 'Top',
	 'widgetType': 'standard'}
	
	apicall = rq.post(url,auth=authDexter,headers=headers,data=json.dumps(payload))
	print apicall.status_code
	dataframe = pd.read_json(json.dumps(apicall.json()['data'])).set_index('name')
	dataframe['movietitle'] = filtername
	return dataframe
	
def main():
	username = raw_input('Enter User Name --> ')
	password = raw_input('Enter Password --> ')
	authDexter=(username,password)
	frames=[]
	failures= []
	for movie in movienames:
		try:
			frames.append(themeApiCalls(url,authDexter,headers,filtername=movie))
		except ValueError:
			failures.append(movie)
			print movie
			pass
	
		
if __name__ == '__main__':
	main()
	
	
	
	