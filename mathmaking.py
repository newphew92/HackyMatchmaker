import csv
import json
from geopy.geocoders import Nominatim

from sklearn.neighbors import NearestNeighbors
import numpy as np

DEBUG = False
WEIGHT = 10000
LINESTART = 0
geolocator = Nominatim(user_agent="SALMatchmaking")
def debug (content):
	if (DEBUG):
		print (content)


dataSet = []
prospectSet = []
targetSet = []

with open('SALentine firesale.csv', mode='r') as csvFile:
	csvReader = csv.DictReader(csvFile)
	lineCount = 0
	for row in csvReader:
		lineCount+=1
		if (lineCount < LINESTART):
			continue
		city = row['Which city are you in?']
		age = row['Age?']
		loc = geolocator.geocode(city, timeout=None)
		if (loc is not None):
			lat = loc.latitude
			lon = loc.longitude
		else:
			lat = 0
			lon = 0
		print(lat,lon)
		dataSet.append({row['Username']:[age, row["Gender you're interested in?"], city, row['Facebook URL']]})
		# debug (row)
# debug (dataSet)
		prospectSet.append([float(age), hash(row["Gender you're interested in?"]), lat, lon])
		targetSet.append([float(age), hash(row['Gender?']), lat, lon])
		print(lineCount)
# print (prospectSet)

samplePoint = {'Username': 't@t.com', 'Age?': '23', 'Timestamp': '2019/02/14 2:27:00 AM EST', "Gender you're interested in?": 'Female', 'Gender?': 'Male', 'Facebook URL': 'https://www.facebook.com/ryanjay.abrigo', 'Which city are you in?': 'Toronto'}
# 'Username'
# 'Age?'
# "Gender you're interested in?"
# 'Gender?'
# 'Which city are you in?'
sampleFeatures = [[float(samplePoint['Age?']), hash(samplePoint["Gender you're interested in?"]), geolocator.geocode(row['Which city are you in?']).latitude, geolocator.geocode(row['Which city are you in?']).longitude]]

n = NearestNeighbors(n_neighbors=5, algorithm='brute').fit(targetSet)
distances, indices = n.kneighbors(prospectSet)
debug(distances)
debug(indices)

with open('SalMailingList.csv', mode='w') as writeFile:
	x = 0
	for prospect in dataSet:
		matches =[]
		for j in indices[x]:
			matches.append(dataSet[j].values()[0][-1])
		print (matches)		
		writeFile.write(json.dumps({dataSet[j].keys()[0]: matches}))
		writeFile.write('\n')
		x += 1

# print (matches)





