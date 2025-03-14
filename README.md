# IoT Light Control System

A simple web-based IoT light control system using MQTT protocol. The system consists of a web interface to control the light and a Python script that simulates an IoT device (ESP8266).

## Components

1. Web Interface (index.html)
   - Provides ON/OFF buttons to control the light
   - Shows connection status
   - Uses MQTT.js for communication

2. IoT Device Simulator (light_simulation.py)
   - Simulates an ESP8266 device
   - Subscribes to MQTT topics
   - Displays light status changes

## Setup and Running

1. Install Python dependencies:
   ```bash
   pip install paho-mqtt
   ```

2. Run the IoT device simulator:
   ```bash
   python light_simulation.py
   ```

3. Open index.html in a web browser

## MQTT Details
- Broker: broker.emqx.io
- Topic: /student_group/light_control
- Port: 1883 (TCP), 8084 (WebSocket) 