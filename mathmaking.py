import csv
import json
from geopy.geocoders import Nominatim
from time  import sleep

from sklearn.neighbors import NearestNeighbors
import numpy as np

DEBUG = True
WEIGHT = 10000
LINESTART = 0
geolocator = Nominatim(user_agent="SALMatchmaker")
def debug (content):
	if (DEBUG):
		print (content)


dataSet = []
prospectSet = []
targetSet = []


def parseRaw(skip=True):
	if skip is True:
		return
	with open('SALentine firesale.csv', mode='r') as csvFile:
		csvReader = csv.DictReader(csvFile)
		lineCount = 0
		cityCache = ''
		longCache = 0.
		latCache = 0.
		for row in csvReader:
			city = row['Which city are you in?']
			age = row['Age?']
			if (cityCache == city):
				print ("Using cache")
				lat = latCache
				lon = longCache
			else:
				print ("fetching geocode")
				loc = geolocator.geocode(city, timeout=None)
				sleep(5)
				if (loc is not None):
					lat = loc.latitude
					lon = loc.longitude
				else:
					lat = 0
					lon = 0
				print(lat,lon)
			debug(lineCount)
			debug(row)
			with open('DataSet.csv', mode='a') as dataFile:
				item = {'Email Address':row['Email Address'], 'Age':age, 'Target':hash(row["Gender you're interested in?"]), 'Source': hash(row['Gender?']),'City':city, 'Long':lon, 'Lat':lat,'FB':row['Facebook URL']}
				dataFile.write(json.dumps(item))
				dataFile.write('\n')

			# dataSet.append({row['Email Address']:[age, row["Gender you're interested in?"], city, row['Facebook URL']]})
	# debug (dataSet)
			lineCount+=1
			cityCache = city
			longCache = lon
			latCache = lat
	# print (prospectSet)

samplePoint = {'Email Address': 't@t.com', 'Age?': '23', 'Timestamp': '2019/02/14 2:27:00 AM EST', "Gender you're interested in?": 'Female', 'Gender?': 'Male', 'Facebook URL': 'https://www.facebook.com/ryanjay.abrigo', 'Which city are you in?': 'Toronto'}
# 'Email Address'
# 'Age?'
# "Gender you're interested in?"
# 'Gender?'
# 'Which city are you in?'
# sampleFeatures = [[float(samplePoint['Age?']), hash(samplePoint["Gender you're interested in?"]), geolocator.geocode(row['Which city are you in?']).latitude, geolocator.geocode(row['Which city are you in?']).longitude]]

def readData():
	with open('DataSet.csv', mode='r') as dataFile:
		csvReader = csv.DictReader(dataFile)
		for row in csvReader:
			prospectSet.append([row['Age'], row['Target'], row['Source'], row['Lat'], row['Long']])
			targetSet.append([row['Age'], row['Target'], row['Target'], row['Lat'], row['Long']])


parseRaw(False)
readData()
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





