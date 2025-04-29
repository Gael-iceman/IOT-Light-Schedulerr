import asyncio
import websockets
import json
import subprocess

MQTT_TOPIC = "light/schedule"
MQTT_BROKER = "localhost"  # change if needed

async def handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        on_time = data['on']
        off_time = data['off']
        payload = f"{on_time},{off_time}"
        print(f"Received schedule: {payload}")

        # Publish to MQTT
        subprocess.run([
            "mosquitto_pub",
            "-h", MQTT_BROKER,
            "-t", MQTT_TOPIC,
            "-m", payload
        ])
        print(f"Published to MQTT: {payload}")

async def main():
    async with websockets.serve(handler, "localhost", 6789):
        print("WebSocket Server started at ws://localhost:6789")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
