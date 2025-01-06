FROM python:3.9-slim  
WORKDIR /app  
COPY data_adapter.py .  
RUN pip install pymongo paho-mqtt pandas  
CMD ["python", "data_adapter.py"]  
