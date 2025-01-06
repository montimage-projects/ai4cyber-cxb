# ai4cyber-cxb
AI4TRIAGE - CXB Use Case
# Dockerized AI4TRIAGE CXB Use Case

## Overview
This project processes log files (firewall, mail, proxy, XDR) and visualizes them through Node-RED. Data is stored in MongoDB and live updates are published via MQTT.

## Setup
1. Clone the repository.  
2. Ensure Docker and Docker Compose are installed.  
3. Run the following command:  
docker-compose up –build
4. Access Node-RED at `http://localhost:1880`.

## Data Flow
1. Logs in CSV format are processed by a Python adapter.  
2. Data is pushed to MongoDB and MQTT.  
3. Node-RED dashboards display alerts and statistics.  
