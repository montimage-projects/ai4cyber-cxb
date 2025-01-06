import pandas as pd  
from sklearn.ensemble import IsolationForest  
from pymongo import MongoClient  

client = MongoClient("mongodb://mongodb:27017/")  
db = client.log_stats  

model = IsolationForest().fit(pd.read_csv('../data/firewall_logs.csv'))  

def analyze():  
    new_data = pd.read_csv('../data/firewall_logs.csv')  
    anomalies = model.predict(new_data)  
    db.anomalies.insert_one({"anomalies": anomalies.tolist()})  

analyze()  
