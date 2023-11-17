#
import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"

def on_message(client, userdata, msg):
    msg = msg.payload.decode()
    if msg == "123456":
        print(f"Received message: {msg}. Exiting...")
        exit(0)
    else:
        print(f"Received message: {msg}")

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, 1883, 60)
client.subscribe("rpi2023fall/msg")
client.loop_forever()
