# Stations API
## Description
This program makes calls to the noaa api to get all the stations that can record data on water levels and tide predictions respectively. The csv files are included in the repository.


## Modifying the API call
```python
>>>import requests
>>>import json
>>>import csv
>>>response = requests.get("https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations.json?type=tidepredictions")
>>>json_res=response.json()
```
If you want to change the type of stations that are collected change the type=tidepredictions to any of the following:
<br>
1.
```python
type=waterlevels
```
2.
```python
type=tidepredictions
```
3.
```python
type=currents
```
4.
```python
type=currentpredictions
```
