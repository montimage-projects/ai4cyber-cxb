import pandas as pd  
from pymongo import MongoClient  
import paho.mqtt.client as mqtt  

client = MongoClient("mongodb://mongodb:27017/")  
db = client.log_stats  
mqtt_client = mqtt.Client()  
mqtt_client.connect("mqtt", 1883, 60)  

def process_logs(file):  
    logs = pd.read_csv(f'../data/{file}')  
    stats = logs.describe()  
    db.logs.insert_one(stats.to_dict())  
    mqtt_client.publish("logs/stats", stats.to_json())  

process_logs("firewall_logs.csv")  
