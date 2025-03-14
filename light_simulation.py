import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("/student_group/light_control")

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    if message == "ON":
        print("💡 Light is TURNED ON")
    elif message == "OFF":
        print("💡 Light is TURNED OFF")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("broker.emqx.io", 1883, 60)

# Start the loop
client.loop_forever() 