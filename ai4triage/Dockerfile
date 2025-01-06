FROM python:3.9-slim  
WORKDIR /app  
COPY ai4triage.py .  
COPY model/anomaly_model.pkl ./model/  
RUN pip install scikit-learn pandas pymongo paho-mqtt  
CMD ["python", "ai4triage.py"]  
