import requests
import json
import csv

response = requests.get("https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations.json?type=waterlevels")
json_res=response.json()

#get the list of all the stations
stations=json_res['stations']

#make a list to store the new station dictionaries in
stations_list=[]

#put the number of stations in the list into
count=json_res['count']
for i in range(0,(count-1)):
    single_station=stations[i]
    station_dict={
        'id':single_station['id'],
        'name':single_station['name'],
        'lat':single_station['lat'],
        'lng':single_station['lng']
        }
    stations_list.append(station_dict)


csv_columns=['id','name','lat','lng']

csv_file = "stations_waterlevels.csv"
try:
    with open(csv_file, 'w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in stations_list:
            # print(data)
            # print(f"data type: {type(data)}")
            writer.writerow(data)
except IOError:
    print("I/O error")
