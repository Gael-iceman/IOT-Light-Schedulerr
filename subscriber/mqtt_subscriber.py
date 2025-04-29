import paho.mqtt.client as mqtt
import serial
import time

SERIAL_PORT = '/dev/ttyACM0'  # Change based on your system
BAUD_RATE = 9600
MQTT_TOPIC = "light/schedule"
MQTT_BROKER = "localhost"

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

def on_connect(client, userdata, flags, rc):
    print(f"Connected with code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Received: {payload}")
    on_time, off_time = payload.split(',')

    # Send to Arduino
    ser.write(f"{on_time},{off_time}\n".encode())
    print(f"Sent to Arduino: {on_time},{off_time}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)
client.loop_forever()
