#
import paho.mqtt.client as mqtt
from time import sleep

broker = "broker.emqx.io"

client = mqtt.Client()
client.connect(broker, 1883, 60)
client.publish("rpi2023fall/4b1g0078/msg", "1.Hello, MQTT!")
client.publish("rpi2023fall/4b1g0078/msg", "2.Hello, MQTT!")
client.publish("rpi2023fall/4b1g0078/msg", "3.Hello, MQTT!")
sleep(1)
client.disconnect()