from pymongo import MongoClient
from django.utils import timezone
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
load_dotenv()

class MongoDBProcessor:
    def __init__(self):
        self.client = MongoClient(os.getenv('mongodb_uri'))
        self.db = self.client['smartcity']
        self.iot_collection = self.db['iot']
        
    def get_congestions_given_time(self, time):
        congestion_info = {"congestions": {"0":[], "1":[], "2":[], "3":[], "4":[], "5":[], "6":[], "7":[], "8":[], "9":[], "10":[], "11":[], "12":[]}}
        for iot in self.iot_collection.find():
            record_index = timedelta(minutes=datetime.strptime(time, "%Y-%m-%dT%H:%M:%S").hour * 60 + datetime.strptime(time, "%Y-%m-%dT%H:%M:%S").minute) // timedelta(minutes=5) - 1
            if len(iot['timeseries']) < 288 or not iot['timeseries'][record_index]['Speed'] or iot['timeseries'][record_index]['Speed'] >= 30:
                continue
            print(iot['timeseries'][record_index]['Speed'])
            data = {
                'latitude': iot['location'][0],
                'longitude': iot['location'][1],
                'location' : str(iot['Fwy']) + ' ' + str(iot['Dir']),
                'dist_id': iot['District'],
                'timestamp': time,
                'speed': iot['timeseries'][record_index]['Speed'],
                'type': 'congestion'
            }
            congestion_info["congestions"][str(iot['District'])].append(data)
            congestion_info["congestions"]["0"].append(data)
        return congestion_info