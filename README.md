💡 Web-Based Light Scheduler with WebSocket and MQTT
📜 Overview
This project simulates a real-world IoT Light Scheduler using:

WebSockets for real-time communication

MQTT for lightweight messaging

Python, HTML/CSS/JavaScript, and Arduino for hardware interaction.

Users can schedule light ON and OFF times through a web interface.
The schedules are forwarded through a WebSocket server, published to an MQTT broker, received by a Python subscriber, and finally sent via serial communication to an Arduino board controlling a physical light relay.

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript (WebSocket API)

Backend: Python (websockets, paho-mqtt, subprocess)

Messaging: Mosquitto MQTT Broker (mosquitto_pub, mosquitto_sub)

Hardware: Arduino UNO, Relay, DS3231 RTC Module

Other Tools: Serial Communication (USB)


📂 Project Structure
bash
Copy
Edit
project/
├── frontend/
│   └── index.html          # Web Interface
├── server/
│   └── websocket_server.py # WebSocket -> MQTT Publisher
├── subscriber/
│   └── mqtt_subscriber.py  # MQTT Subscriber -> Arduino Serial
└── arduino/
    └── light_control.ino   # Arduino Sketch for Light Control


    🚀 Installation & Setup
Install MQTT Broker (Mosquitto)

sudo apt install mosquitto mosquitto-clients


Install Python Libraries

pip install websockets paho-mqtt pyserial

Upload Arduino Code

Connect your Arduino.

Open light_control.ino in Arduino IDE.

Select correct COM port and upload the sketch.

Ensure an RTC module (DS3231) is connected if using real time.

Start MQTT Broker

mosquitto



Run WebSocket Server

cd server
python websocket_server.py

Run MQTT Subscriber

cd subscriber
python mqtt_subscriber.py

Open the Frontend

Open frontend/index.html in your browser.

Enter ON and OFF times and click Submit.

⚙️ Configuration Notes
Serial Port:
Change the SERIAL_PORT in mqtt_subscriber.py to match your Arduino's port.
(Example: /dev/ttyACM0 on Linux, COM3 on Windows.)

Broker IP:
Update MQTT_BROKER in both server and subscriber if not running locally.

Time Sync:
Ensure Arduino time matches the timezone you're submitting from.
If no RTC, fake time in code.

👨‍💻 Author
Built by: RUTAYISIRE Gael
Contact: rutayisiregael2000@gmail.com
